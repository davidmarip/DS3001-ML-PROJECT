#!/usr/bin/env python3
"""
Convert existing HTML plots to PNG format
This script reads existing HTML Plotly files and generates PNG versions
"""

import plotly.io as pio
import plotly.graph_objects as go
from pathlib import Path
import json
import re

def convert_html_to_png(html_path, png_path):
    """Convert HTML Plotly file to PNG"""
    try:
        # Read HTML file
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract the Plotly data (this is a simplified approach)
        # Look for the plotly data in the HTML
        fig_data_match = re.search(r'Plotly\.newPlot\([^,]+,\s*(\[.*?\]),\s*(\{.*?\})', html_content, re.DOTALL)
        
        if fig_data_match:
            # This is a complex extraction - for safety, we'll use a different approach
            # Load the figure using plotly.io
            fig = pio.from_html(html_content)
            
            # Save as PNG
            fig.write_image(png_path, width=1200, height=800, scale=2)
            print(f"Converted {html_path.name} -> {png_path.name}")
            return True
        else:
            print(f"Could not extract figure data from {html_path.name}")
            return False
            
    except Exception as e:
        print(f"Error converting {html_path.name}: {e}")
        return False

def main():
    """Convert all HTML files in figures directory to PNG"""
    
    figures_dir = Path('../RESULTS/figures')
    
    if not figures_dir.exists():
        print("RESULTS/figures directory not found")
        return
    
    # Find all HTML files
    html_files = list(figures_dir.glob('*.html'))
    
    if not html_files:
        print("No HTML files found in figures directory")
        return
    
    print(f"Found {len(html_files)} HTML files to convert...")
    
    converted = 0
    failed = 0
    
    for html_file in html_files:
        png_file = html_file.with_suffix('.png')
        
        # Skip if PNG already exists and is newer
        if png_file.exists() and png_file.stat().st_mtime > html_file.stat().st_mtime:
            print(f"PNG already up to date: {png_file.name}")
            continue
        
        if convert_html_to_png(html_file, png_file):
            converted += 1
        else:
            failed += 1
    
    print(f"\nConversion complete!")
    print(f"Successfully converted: {converted}")
    print(f"Failed: {failed}")
    
    if failed > 0:
        print("\nNote: Some conversions failed. You may need to re-run the notebooks")
        print("with the updated plotting functions to generate both HTML and PNG.")

if __name__ == "__main__":
    main()