import os # Allows us to interact with operating system.
import re # Provides support for regular expressions. 
# When making comments make sure to use PEP 8. 
# This assignment is to create a website and add comments to better understand the components. 

# Slugify function I understand how this works and why we use it. 
def slugify(title):
    """Convert the page title to a filename-friendly slug."""
    if title.lower() == "home":  # Ensure 'Home' becomes 'index.html' where if statement is. 
        return "index.html"
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html"
# Regular expression line 11. 

# Nav funciton.
def generate_nav(titles, active_title):
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""
    for title in titles:
        # For loop. 
        filename = slugify(title)
        active_class = ' class="active"' if title == active_title else ""
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n'
    return nav_links.strip()
# F-string on line 21.

# Create html function.
def create_html_file(title, titles, output_dir="build"):
    """Generate and write HTML content based on the page title."""
    filename = slugify(title)
    nav = generate_nav(titles, active_title=title)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav>
            {nav}
        </nav>
        <div class="content">
            <h1>{title}</h1>
            <p>This is the {title.lower()} content.</p>
        </div>
    </body>
    </html>
    """
# I understand why we use this portion for the assignment.  
    output_path = os.path.join(output_dir, filename)
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists also where directory is. 

    with open(output_path, 'w') as file:
        file.write(html_content)
        # With open on line 55 file write on line 56.

    print(f"Created {filename} in the '{output_dir}' directory.")

    # Create CSS file function this styles our website. 
def create_css_file(output_dir="build"):
    """Generate and write the style.css file based on a dictionary of styles."""
    styles = {
        "font-family": "Calibri",             # font family
        "body-background": "#7BAFD4",     # Background color for .content
        "nav-background": "#13294B",          # Background color for nav
        "nav-a-color": "#4B9CD3",              # Text color for nav links
        "nav-a-active-color": "#ffffff"
    # Dictionary. 
    }
# CSS content adds decoration/fonts/colors to make our website more exciting. 
    css_content = f"""
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: {styles["font-family"]};
    }}

    body {{
        background-color: {styles["body-background"]};
    }}

    nav {{
        background-color: {styles["nav-background"]};
        padding: 10px;
    }}

    nav a {{
        color: {styles["nav-a-color"]};
        margin-right: 10px;
        text-decoration: none;
    }}

    nav a.active {{
        color: {styles["nav-a-active-color"]};
        font-weight: bold;
    }}

    .content {{
        background-color: #F8F8F8;
        padding: 20px;
        margin: 20px;
    }}
    """
# Allows css to be able to be opened. 
    css_path = os.path.join(output_dir, "style.css")
    with open(css_path, 'w') as file:
        file.write(css_content)

    print(f"Created style.css in the '{output_dir}' directory.")

    # Create main function I changed my names to personalize them. 
def main():
    """Main function to generate pages and styles. MUST HAVE HOME!!!"""
    titles = ["Home", "About Family", "My Favorite Places", "Restaurants"]

    # Create HTML files for each title
    for title in titles:
        create_html_file(title, titles)

    # Create the style.css file
        create_css_file() 
    # uncomment the create_css_file() function if you add the function.

if __name__ == "__main__":
    main()
    # Where method is and this was a fun project. 
    # Pass statement is in our original code but not CSS code. 


