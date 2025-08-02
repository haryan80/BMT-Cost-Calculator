#!/usr/bin/env python3
"""
Simple development server for testing Azure AD authentication
Run this script to serve the BMT Cost Calculator locally
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 4280

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers for development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        super().end_headers()

def main():
    # Change to the directory containing the HTML file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    # Check if the HTML file exists
    html_file = "BMT Cost Calculator.html"
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found in {script_dir}")
        sys.exit(1)
    
    # Create server
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Starting development server on http://localhost:{PORT}")
        print(f"📁 Serving files from: {script_dir}")
        print(f"🌐 Open your browser to: http://localhost:{PORT}")
        print(f"📄 Main file: http://localhost:{PORT}/{html_file}")
        print("\n⚠️  Important for Azure AD:")
        print("   - Make sure your Azure AD app registration includes:")
        print(f"     Redirect URI: http://localhost:{PORT}")
        print("   - Update the msalConfig in the HTML file with your Azure AD details")
        print("\n🛑 Press Ctrl+C to stop the server")
        
        try:
            # Open browser automatically
            webbrowser.open(f"http://localhost:{PORT}/{html_file}")
            
            # Start server
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped by user")
        except Exception as e:
            print(f"❌ Error starting server: {e}")

if __name__ == "__main__":
    main() 