import socketserver
import http.server
import urllib.parse

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        print(f"Received GET request for path: {path}")

        if path == '/':  # Serve index.html
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            try:
                with open("index.html", "rb") as file:
                    self.wfile.write(file.read())
                print("Response 200: Served index.html")
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
                print("Response 404: index.html not found")

        elif path == '/styles.css':  # Serve styles.css
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            try:
                with open("styles.css", "rb") as file:
                    self.wfile.write(file.read())
                print("Response 200: Served styles.css")
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
                print("Response 404: styles.css not found")

        else:  # Handle other paths with 404
            self.send_error(404)
            print(f"Response 404: Path {path} not found")


if __name__ == "__main__":
    server_address = ("localhost", 8080)  # The server will listen on localhost:8080
    httpd = socketserver.TCPServer(server_address, MyHandler)  # Create a new server
    
    # Print the message when the server starts
    print("Server is running at http://localhost:8080")
    print("Press Ctrl+C to stop the server.")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
        httpd.server_close()
        print("Server stopped.")
