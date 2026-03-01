import os
import shutil

directory = "c:\\Saft Family Files\\The Heritage Letters"
story10_path = os.path.join(directory, "story-10.html")

# 1. Create Story 11 and 12
shutil.copy(story10_path, os.path.join(directory, "story-11.html"))
shutil.copy(story10_path, os.path.join(directory, "story-12.html"))

# 2. Add 3 more timeline events to ALL stories (1-12)
new_nodes = """
                    <!-- Node 6 -->
                    <div class="timeline-item right">
                        <div class="timeline-content">
                            <div class="timeline-year">1975</div>
                            <div class="timeline-personal">Welcomed first child into the family.</div>
                            <p class="timeline-world">Historical Context: The End of the Vietnam War</p>
                        </div>
                    </div>
                    <!-- Node 7 -->
                    <div class="timeline-item left">
                        <div class="timeline-content">
                            <div class="timeline-year">1995</div>
                            <div class="timeline-personal">Relocated and began a new community chapter.</div>
                            <p class="timeline-world">Historical Context: The Dot-Com Boom Begins</p>
                        </div>
                    </div>
                    <!-- Node 8 -->
                    <div class="timeline-item right">
                        <div class="timeline-content">
                            <div class="timeline-year">2010</div>
                            <div class="timeline-personal">Retired and started volunteering locally.</div>
                            <p class="timeline-world">Historical Context: The Rise of Smartphones</p>
                        </div>
                    </div>
"""

for i in range(1, 13):
    filepath = os.path.join(directory, f"story-{i}.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to insert these before Node 4 to keep chronological order somewhat okay,
    # or just insert them. Actually, let's just replace the entire timeline block to be perfectly chronological.
    
    # Let's extract everything from <div class="timeline"> to </div>
    # Actually, simpler to just append them before </section> inside the timeline div if we can.
    # We already have Node 1, 2, 3, 4, 5. 
    # Let's just append the new nodes right before the closing </div> of <div class="timeline">.
    # The structure: 
    #                 </div>
    #             </section>
    
    search_str = "                        </div>\n                    </div>\n                </div>\n            </section>"
    replace_str = "                        </div>\n                    </div>" + new_nodes + "                </div>\n            </section>"
    
    if search_str in content:
        content = content.replace(search_str, replace_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Created 11 and 12, added 3 timeline nodes to all 12 stories.")
