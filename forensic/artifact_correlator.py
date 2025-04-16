#!/usr/bin/env python3
import networkx as nx
import matplotlib.pyplot as plt
import json
import argparse
from collections import defaultdict
import pandas as pd
from datetime import datetime

class ArtifactCorrelator:
    def __init__(self):
        self.artifacts = defaultdict(dict)
        self.relationships = []
        self.graph = nx.Graph()
        
    def add_artifact(self, artifact_id, artifact_type, properties):
        """Add an artifact to the correlation database"""
        self.artifacts[artifact_id] = {
            'type': artifact_type,
            'properties': properties
        }
        self.graph.add_node(artifact_id, **properties)
    
    def add_relationship(self, source_id, target_id, relationship_type, properties=None):
        """Add a relationship between artifacts"""
        self.relationships.append({
            'source': source_id,
            'target': target_id,
            'type': relationship_type,
            'properties': properties or {}
        })
        self.graph.add_edge(source_id, target_id, 
                          type=relationship_type,
                          **properties or {})
    
    def correlate(self):
        """Correlate artifacts based on their properties and relationships"""
        # Find direct relationships
        direct_correlations = self._find_direct_correlations()
        
        # Find indirect relationships
        indirect_correlations = self._find_indirect_correlations()
        
        return {
            'direct': direct_correlations,
            'indirect': indirect_correlations
        }
    
    def _find_direct_correlations(self):
        """Find direct correlations between artifacts"""
        correlations = []
        
        # Look for artifacts with matching properties
        for id1, artifact1 in self.artifacts.items():
            for id2, artifact2 in self.artifacts.items():
                if id1 >= id2:  # Avoid duplicate comparisons
                    continue
                    
                # Find matching properties
                matches = []
                for prop, value in artifact1['properties'].items():
                    if prop in artifact2['properties']:
                        if artifact2['properties'][prop] == value:
                            matches.append(prop)
                
                if matches:
                    correlations.append({
                        'source': id1,
                        'target': id2,
                        'matching_properties': matches
                    })
        
        return correlations
    
    def _find_indirect_correlations(self):
        """Find indirect correlations through relationships"""
        indirect_correlations = []
        
        # Use networkx to find paths between artifacts
        for source in self.graph.nodes():
            for target in self.graph.nodes():
                if source >= target:  # Avoid duplicate paths
                    continue
                    
                try:
                    paths = list(nx.all_shortest_paths(self.graph, source, target))
                    if len(paths) > 1:  # Multiple paths indicate strong correlation
                        indirect_correlations.append({
                            'source': source,
                            'target': target,
                            'paths': paths
                        })
                except nx.NetworkXNoPath:
                    continue
        
        return indirect_correlations
    
    def visualize_correlations(self, output_file='correlations.png'):
        """Generate a visualization of the artifact correlations"""
        plt.figure(figsize=(12, 8))
        
        # Draw the graph
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue',
                node_size=2000, font_size=8, font_weight='bold')
        
        # Add edge labels
        edge_labels = nx.get_edge_attributes(self.graph, 'type')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        
        plt.title('Artifact Correlation Graph')
        plt.savefig(output_file)
        print(f"Correlation graph saved to {output_file}")
    
    def export_correlations(self, format='json'):
        """Export correlations in the specified format"""
        correlations = self.correlate()
        
        if format == 'json':
            with open('correlations.json', 'w') as f:
                json.dump(correlations, f, indent=2)
            print("Correlations exported to correlations.json")
            
        elif format == 'csv':
            # Convert to DataFrame
            rows = []
            for corr in correlations['direct']:
                rows.append({
                    'source': corr['source'],
                    'target': corr['target'],
                    'type': 'direct',
                    'matching_properties': ','.join(corr['matching_properties'])
                })
            
            for corr in correlations['indirect']:
                rows.append({
                    'source': corr['source'],
                    'target': corr['target'],
                    'type': 'indirect',
                    'paths': str(corr['paths'])
                })
            
            df = pd.DataFrame(rows)
            df.to_csv('correlations.csv', index=False)
            print("Correlations exported to correlations.csv")

def main():
    parser = argparse.ArgumentParser(description='Correlate digital artifacts across different sources')
    parser.add_argument('--visualize', action='store_true',
                      help='Generate visualization of correlations')
    parser.add_argument('--export', choices=['json', 'csv'],
                      default='json', help='Export format for correlations')
    args = parser.parse_args()
    
    correlator = ArtifactCorrelator()
    
    # Example usage
    correlator.add_artifact('file1', 'document', {
        'filename': 'report.docx',
        'author': 'John Doe',
        'created': '2023-01-01'
    })
    
    correlator.add_artifact('file2', 'document', {
        'filename': 'notes.txt',
        'author': 'John Doe',
        'created': '2023-01-02'
    })
    
    correlator.add_artifact('user1', 'user', {
        'username': 'jdoe',
        'email': 'john.doe@example.com'
    })
    
    correlator.add_relationship('file1', 'user1', 'created_by')
    correlator.add_relationship('file2', 'user1', 'created_by')
    
    if args.visualize:
        correlator.visualize_correlations()
    
    correlator.export_correlations(args.export)

if __name__ == '__main__':
    main() 