import os

directory = "c:\\Saft Family Files\\The Heritage Letters"

mapping = {
    8: ('mateo', "images/mateo_youth.png", "https://picsum.photos/seed/mateo_present/1920/1080"),
    9: ('iris', "https://picsum.photos/seed/iris_youth/400/600", "https://picsum.photos/seed/iris_present/1920/1080"),
    10: ('thomas', "https://picsum.photos/seed/thomas_youth/400/600", "https://picsum.photos/seed/thomas_present/1920/1080"),
    11: ('david', "https://picsum.photos/seed/david_youth/400/600", "https://picsum.photos/seed/david_present/1920/1080"),
    12: ('sarah', "https://picsum.photos/seed/sarah_youth/400/600", "https://picsum.photos/seed/sarah_present/1920/1080")
}

for i, (name, youth_url, present_url) in mapping.items():
    filepath = os.path.join(directory, f"story-{i}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Hero Image
    hero_search = """    <div class="article-hero-image">
        [Present Day Portrait Placeholder]
    </div>"""
    
    # If the hero image doesn't match perfectly, let's use a simpler replace
    content = content.replace(hero_search, f"""    <div class="article-hero-image" style="background-image: url('{present_url}'); background-size: cover; background-position: center; color: transparent;">
        {name} Present Day
    </div>""")
    
    # 2. Update Side Image (Youth)
    # Story 8 already has the mateo_youth image mostly, but others usually have:
    """                <div class="side-image">
                    [Youth Photo Placeholder]
                </div>"""
                
    # just in case we need to overwrite existing side-image styles
    import re
    
    # Replace the whole side-image block
    filter_style = " filter: grayscale(1) sepia(0.2);" if "picsum" in youth_url else ""
    
    side_img_pattern = re.compile(r'<div class="side-image".*?>.*?</div>', re.DOTALL)
    new_side_img = f"""<div class="side-image" style="background-image: url('{youth_url}'); background-size: cover; background-position: center; color: transparent;{filter_style}">
                    {name} Youth
                </div>"""
    content = re.sub(side_img_pattern, new_side_img, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated images for stories 8-12.")
