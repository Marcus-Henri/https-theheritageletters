import os

directory = "c:\\Saft Family Files\\The Heritage Letters"
for i in range(1, 11):
    filename = os.path.join(directory, f"story-{i}.html")
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    new_nodes = """
                    <!-- Node 4 -->
                    <div class="timeline-item right">
                        <div class="timeline-content">
                            <div class="timeline-year">2001</div>
                            <div class="timeline-personal">Embraced the digital age and reconnected with old friends.</div>
                            <p class="timeline-world">Historical Context: The Rise of the Internet</p>
                        </div>
                    </div>
                    <!-- Node 5 -->
                    <div class="timeline-item left">
                        <div class="timeline-content">
                            <div class="timeline-year">2020</div>
                            <div class="timeline-personal">Navigated unprecedented times with quiet resilience.</div>
                            <p class="timeline-world">Historical Context: Global Pandemic</p>
                        </div>
                    </div>
"""

    search_str = "                        </div>\n                    </div>\n                </div>\n            </section>"
    replace_str = "                        </div>\n                    </div>" + new_nodes + "                </div>\n            </section>"
            
    if search_str in content:
        content = content.replace(search_str, replace_str)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"Could not find injection point in {filename}")
