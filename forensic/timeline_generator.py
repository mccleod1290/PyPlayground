#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import argparse
import json
import os
from dateutil import parser as date_parser
import pytz

class TimelineGenerator:
    def __init__(self):
        self.events = []
        self.timezone = pytz.UTC  # Default to UTC
        
    def add_event(self, timestamp, source, event_type, description, metadata=None):
        """Add an event to the timeline"""
        try:
            if isinstance(timestamp, str):
                timestamp = date_parser.parse(timestamp)
            if timestamp.tzinfo is None:
                timestamp = self.timezone.localize(timestamp)
                
            self.events.append({
                'timestamp': timestamp,
                'source': source,
                'type': event_type,
                'description': description,
                'metadata': metadata or {}
            })
        except Exception as e:
            print(f"Error adding event: {str(e)}")
    
    def set_timezone(self, timezone_str):
        """Set the timezone for the timeline"""
        try:
            self.timezone = pytz.timezone(timezone_str)
        except pytz.exceptions.UnknownTimeZoneError:
            print(f"Unknown timezone: {timezone_str}. Using UTC instead.")
            self.timezone = pytz.UTC
    
    def generate_timeline(self, output_format='text'):
        """Generate the timeline in the specified format"""
        if not self.events:
            print("No events to generate timeline from")
            return
            
        # Sort events by timestamp
        self.events.sort(key=lambda x: x['timestamp'])
        
        if output_format == 'text':
            self._generate_text_timeline()
        elif output_format == 'csv':
            self._generate_csv_timeline()
        elif output_format == 'json':
            self._generate_json_timeline()
        elif output_format == 'plot':
            self._generate_visual_timeline()
        else:
            print(f"Unknown output format: {output_format}")
    
    def _generate_text_timeline(self):
        """Generate a text-based timeline"""
        print("\n=== Timeline Analysis ===")
        for event in self.events:
            print(f"\nTimestamp: {event['timestamp']}")
            print(f"Source: {event['source']}")
            print(f"Type: {event['type']}")
            print(f"Description: {event['description']}")
            if event['metadata']:
                print("Metadata:")
                for key, value in event['metadata'].items():
                    print(f"  {key}: {value}")
            print("---")
    
    def _generate_csv_timeline(self):
        """Generate a CSV timeline"""
        df = pd.DataFrame(self.events)
        df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S %Z')
        df.to_csv('timeline.csv', index=False)
        print("Timeline saved to timeline.csv")
    
    def _generate_json_timeline(self):
        """Generate a JSON timeline"""
        timeline_data = []
        for event in self.events:
            event_data = event.copy()
            event_data['timestamp'] = event['timestamp'].isoformat()
            timeline_data.append(event_data)
            
        with open('timeline.json', 'w') as f:
            json.dump(timeline_data, f, indent=2)
        print("Timeline saved to timeline.json")
    
    def _generate_visual_timeline(self):
        """Generate a visual timeline plot"""
        plt.figure(figsize=(12, 6))
        
        # Create a timeline plot
        for i, event in enumerate(self.events):
            plt.plot(event['timestamp'], i, 'o', label=event['source'])
            plt.annotate(event['description'], 
                        (event['timestamp'], i),
                        xytext=(10, 0), textcoords='offset points')
        
        plt.title('Event Timeline')
        plt.xlabel('Time')
        plt.ylabel('Event Index')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('timeline.png')
        print("Timeline plot saved to timeline.png")

def main():
    parser = argparse.ArgumentParser(description='Generate timelines from system artifacts')
    parser.add_argument('--format', choices=['text', 'csv', 'json', 'plot'],
                      default='text', help='Output format for the timeline')
    parser.add_argument('--timezone', default='UTC',
                      help='Timezone for the timeline (default: UTC)')
    args = parser.parse_args()
    
    generator = TimelineGenerator()
    generator.set_timezone(args.timezone)
    
    # Example usage
    generator.add_event('2023-01-01 10:00:00', 'System', 'Login',
                       'User login detected', {'user': 'admin'})
    generator.add_event('2023-01-01 10:05:00', 'Network', 'Connection',
                       'Outbound connection established', {'destination': '192.168.1.100'})
    generator.add_event('2023-01-01 10:10:00', 'File System', 'File Access',
                       'Sensitive file accessed', {'filename': 'secret.txt'})
    
    generator.generate_timeline(args.format)

if __name__ == '__main__':
    main() 