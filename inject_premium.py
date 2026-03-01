import glob
import os

audio_html = """            <div class="audio-player-container">
                <span class="audio-player-label">Listen to this story narrated by the author</span>
                <audio class="custom-audio" controls>
                    <source src="#" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>"""

timeline_html = """            <!-- Interactive Timeline Section -->
            <section class="timeline-section">
                <h2 class="timeline-title">A Life in Context</h2>
                <div class="timeline">
                    <!-- Node 1 -->
                    <div class="timeline-item left">
                        <div class="timeline-content">
                            <div class="timeline-year">1945</div>
                            <div class="timeline-personal">Born in Chicago, IL.</div>
                            <p class="timeline-world">Historical Context: World War II Ends</p>
                        </div>
                    </div>
                    <!-- Node 2 -->
                    <div class="timeline-item right">
                        <div class="timeline-content">
                            <div class="timeline-year">1969</div>
                            <div class="timeline-personal">Graduated from University.</div>
                            <p class="timeline-world">Historical Context: Apollo 11 Moon Landing</p>
                        </div>
                    </div>
                    <!-- Node 3 -->
                    <div class="timeline-item left">
                        <div class="timeline-content">
                            <div class="timeline-year">1989</div>
                            <div class="timeline-personal">Started independent business.</div>
                            <p class="timeline-world">Historical Context: Fall of the Berlin Wall</p>
                        </div>
                    </div>
                </div>
            </section>"""

files = glob.glob("story-*.html")
count = 0
for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    new_content = content
    
    # Inject audio
    if '<div class="audio-player-container">' not in new_content:
        new_content = new_content.replace('<div class="content-body">', audio_html + '\n\n            <div class="content-body">')

    # Inject timeline
    if '<section class="timeline-section">' not in new_content:
        new_content = new_content.replace('<hr style="margin: var(--spacing-lg) 0;', timeline_html + '\n\n            <hr style="margin: var(--spacing-lg) 0;')
        
    if new_content != content:
        with open(f, "w", encoding="utf-8") as file:
            file.write(new_content)
        count += 1
        
print(f"Components injected into {count} HTML files.")
