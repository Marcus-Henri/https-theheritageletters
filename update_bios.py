import os

directory = "c:\\Saft Family Files\\The Heritage Letters"
story11_path = os.path.join(directory, "story-11.html")
story12_path = os.path.join(directory, "story-12.html")

# Update Story 11
with open(story11_path, 'r', encoding='utf-8') as f:
    s11 = f.read()

s11 = s11.replace('Born 1948 • Detroit, MI', 'Born 1941 • Taipei, TW')
s11 = s11.replace('Thomas Keller', 'David Chen')
s11 = s11.replace('After thirty years on the assembly line, Tom pivotally changed his life. He discusses the dignity of hard labor and the joy of late-in-life reinvention.', 'From building the first microchips in Silicon Valley to cultivating bonsai trees in his garden. David shares his view on patience and progress.')
s11 = s11.replace('After thirty years in the same factory, tightening thousands of bolts on cars he could rarely afford', 'After thirty-five years working in clean words building the very first microchips that would power the modern world')
s11 = s11.replace('Thomas "Tom" Keller', 'David Chen')
s11 = s11.replace('Tom', 'David')
s11 = s11.replace('images/thomas_youth.png', 'https://picsum.photos/seed/david_youth/400/600')
s11 = s11.replace('images/thomas_present.png', 'https://picsum.photos/seed/david_present/400/600')
s11 = s11.replace('style=""', '') # Clear any empty styles
s11 = s11.replace('img-placeholder" style="background-image: url(\'\')', 'img-placeholder" style="background-image: url(\'https://picsum.photos/seed/david_youth/400/600\'); filter: grayscale(1) sepia(0.2);"')

# We will just globally replace the photo placeholders since they were empty in story-10
if 'background-image: url(\'\');' in s11:
    pass # we might need to be more specific, but let's just use regex or specific strings.

with open(story11_path, 'w', encoding='utf-8') as f:
    f.write(s11)


# Update Story 12
with open(story12_path, 'r', encoding='utf-8') as f:
    s12 = f.read()

s12 = s12.replace('Born 1948 • Detroit, MI', 'Born 1950 • Chicago, IL')
s12 = s12.replace('Thomas Keller', 'Sarah Jenkins')
s12 = s12.replace('After thirty years on the assembly line, Tom pivotally changed his life. He discusses the dignity of hard labor and the joy of late-in-life reinvention.', 'A beloved high-school literature teacher who dedicated thirty-five years to public education. She shares why the classics still matter.')
s12 = s12.replace('After thirty years in the same factory, tightening thousands of bolts on cars he could rarely afford', 'After thirty-five years teaching literature to teenagers who thought they knew everything about the world')
s12 = s12.replace('Thomas "Tom" Keller', 'Sarah Jenkins')
s12 = s12.replace('Tom', 'Sarah')

with open(story12_path, 'w', encoding='utf-8') as f:
    f.write(s12)

print("Updated 11 and 12 text contents.")
