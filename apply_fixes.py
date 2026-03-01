import os
import re

directory = "c:\\Saft Family Files\\The Heritage Letters"

locations = {
    "1932 • Chicago, IL": "Current: New York, NY",
    "1928 • London, UK": "Current: Cotswolds, UK",
    "1940 • Havana, Cuba": "Current: Austin, TX",
    "1938 • Memphis, TN": "Current: Boston, MA",
    "1945 • Kyoto, Japan": "Current: San Francisco, CA",
    "1935 • Montgomery, AL": "Current: Atlanta, GA",
    "1925 • Boston, MA": "Current: Seattle, WA",
    "1942 • San Juan, PR": "Current: Miami, FL",
    "1939 • Stockholm, SE": "Current: Portland, OR",
    "1948 • Detroit, MI": "Current: Grand Rapids, MI",
    "1941 • Taipei, TW": "Current: San Jose, CA",
    "1950 • Chicago, IL": "Current: Evanston, IL",
}

# 1. Update Index.html
index_path = os.path.join(directory, "index.html")
with open(index_path, 'r', encoding='utf-8') as f:
    idx_content = f.read()

for loc_match, current_loc in locations.items():
    idx_content = idx_content.replace(
        f"Born {loc_match}</span>", 
        f"Born {loc_match} | {current_loc}</span>"
    )

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(idx_content)

# 2. Update Story files
for i in range(1, 13):
    filepath = os.path.join(directory, f"story-{i}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for loc_match, current_loc in locations.items():
        content = content.replace(
            f"Born {loc_match}</span>", 
            f"Born {loc_match} | {current_loc}</span>"
        )
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# 3. Completely overhaul story-11 and story-12 text to fix copy-over errors
s11_path = os.path.join(directory, "story-11.html")
s12_path = os.path.join(directory, "story-12.html")

# Story 11 Content Replacements
with open(s11_path, 'r', encoding='utf-8') as f:
    s11 = f.read()

s11_intro_old = r'<p class="article-intro">.*?</p>'
s11_intro_new = """<p class="article-intro">
                    From building the first microchips in Silicon Valley to cultivating bonsai trees in his garden. David shares his view on patience, the relentless march of technology, and finding peace in the slow growth of living things.
                </p>"""
s11 = re.sub(s11_intro_old, s11_intro_new, s11, flags=re.DOTALL)

s11_body_old = r'<div class="content-body">.*?<!-- Interactive Timeline Section -->'
s11_body_new = """<div class="content-body">
                <p class="drop-cap">
                    David Chen arrived in California in 1968 with two suitcases and a degree in electrical engineering. He spent the next three decades in the sterile environment of semiconductor cleanrooms, helping to forge the silicon foundation of the modern digital age. The pace of innovation was blistering, defined by Moore's Law and a relentless drive toward the future. 
                </p>

                <p>
                    "We were building the brains of the new world," David reflects, his hands resting on a beautifully gnarled juniper bonsai. "Everything was about speed, miniaturization, and obsolescence. What is cutting edge today is garbage in five years."
                </p>

                <div class="side-image" style="background-image: url('https://picsum.photos/seed/david_youth/400/600'); background-size: cover; background-position: center; color: transparent; filter: grayscale(1) sepia(0.2);">
                    David Youth
                </div>

                <p>
                    When David retired, the sudden cessation of that frantic pace left him unmoored. He found his anchor not in circuits, but in soil. He dedicated himself to the ancient art of bonsai, a discipline that demands an entirely completely different relationship with time. "A microchip is obsolete in months. A bonsai takes thirty years just to begin showing its true character," he explains.
                </p>

                <p>
                    He discusses how the digital revolution he helped spark has created a world that is overly connected but deeply fractured. His garden offers a sanctuary from the blue light of the screens he once engineered. 
                </p>

                <blockquote>
                    "In engineering, we try to eliminate all variables to achieve perfection. In nature, perfection is found in how a living thing responds to the variables. The bend in the trunk is where the beauty lives."
                </blockquote>

                <p>
                    For the younger generation navigating a hyper-accelerated world, David's message is gentle but firm. "Look at something green every day. Understand that not every problem needs an immediate solution. Sometimes, you just need to water the roots and wait."
                </p>
            </div>

        
                        <!-- Interactive Timeline Section -->"""
s11 = re.sub(s11_body_old, s11_body_new, s11, flags=re.DOTALL)

# Update favorites in 11
s11 = re.sub(r'The defining characteristic of an adult.*?figure out how to build a ladder\."', r'"In engineering, we try to eliminate all variables to achieve perfection. In nature, perfection is found in how a living thing responds to the variables."', s11, flags=re.DOTALL)
s11 = s11.replace('— Sarah Jenkins', '— David Chen')
s11 = s11.replace('Working', 'The Hidden Life of Trees')
s11 = s11.replace('Studs Terkel understood better than anyone that our jobs define our dignity.', 'A brilliant exploration of how the natural world communicates and thrives slowly.')
s11 = s11.replace('Motown, The Temptations', 'Classical, Yo-Yo Ma')
s11 = s11.replace('Rocky', 'Seven Samurai')

with open(s11_path, 'w', encoding='utf-8') as f:
    f.write(s11)


# Story 12 Content Replacements
with open(s12_path, 'r', encoding='utf-8') as f:
    s12 = f.read()

s12_intro_old = r'<p class="article-intro">.*?</p>'
s12_intro_new = """<p class="article-intro">
                    A beloved high-school literature teacher who dedicated thirty-five years to public education. She shares why the classics still matter, the terrifying vulnerability of teenagers, and the enduring power of a good story.
                </p>"""
s12 = re.sub(s12_intro_old, s12_intro_new, s12, flags=re.DOTALL)

s12_body_old = r'<div class="content-body">.*?<!-- Interactive Timeline Section -->'
s12_body_new = """<div class="content-body">
                <p class="drop-cap">
                    For thirty-five years, Sarah Jenkins commanded Room 204 at Lincoln High School. She taught American Literature to thousands of teenagers, translating the anxieties of Holden Caulfield and the ambition of Jay Gatsby for generations of students who often preferred passing notes to parsing metaphors.
                </p>

                <p>
                    "Teaching is an act of spectacular optimism," Sarah says, adjusting her reading glasses. "You are planting seeds in a garden you will likely never see bloom. You have to trust that the water you provide today will sustain them a decade from now."
                </p>

                <div class="side-image" style="background-image: url('https://picsum.photos/seed/sarah_youth/400/600'); background-size: cover; background-position: center; color: transparent; filter: grayscale(1) sepia(0.2);">
                    Sarah Youth
                </div>

                <p>
                    Sarah fiercely defended the necessity of reading fiction in an increasingly pragmatic world. She believed that reading wasn't just about vocabulary; it was an exercise in radical empathy. It forced young minds to occupy the experiences of people wildly unlike themselves.
                </p>

                <p>
                    She recalls the profound impact of having her students relate to characters from centuries past. "When a sixteen-year-old realizes that Shakespeare perfectly articulated the exact heartbreak they experienced at prom, their universe expands. They suddenly realize they are not alone."
                </p>

                <blockquote>
                    "The greatest literature doesn't give you answers. It simply gives you a better, more beautiful set of questions to ask yourself about how to live."
                </blockquote>

                <p>
                    Today, Sarah spends her retirement running a community literacy program. Her faith in the written word remains entirely unshaken. "The medium might change. The screens might glow. But human beings are fundamentally storytelling creatures," she asserts. "As long as there is darkness outside the cave, we will need good stories to make sense of the light." 
                </p>
            </div>

        
                        <!-- Interactive Timeline Section -->"""
s12 = re.sub(s12_body_old, s12_body_new, s12, flags=re.DOTALL)

# Update favorites in 12
s12 = re.sub(r'The defining characteristic of an adult.*?figure out how to build a ladder\."', r'"The greatest literature doesn\'t give you answers. It simply gives you a better, more beautiful set of questions to ask yourself about how to live."', s12, flags=re.DOTALL)
s12 = s12.replace('Working', 'To Kill a Mockingbird')
s12 = s12.replace('Studs Terkel understood better than anyone that our jobs define our dignity.', 'The quintessential American novel about empathy and courage.')
s12 = s12.replace('Motown, The Temptations', 'Folk, Joni Mitchell')
s12 = s12.replace('Rocky', 'Dead Poets Society')

with open(s12_path, 'w', encoding='utf-8') as f:
    f.write(s12)

print("Updated current locations and rewrote story 11 and 12 bodies.")
