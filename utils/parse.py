import markdown



def parse():
    with open("utils/ai_answers.txt", "r", encoding="utf-8") as file:
        text = file.read()
    
    html_output = markdown.markdown(text, extensions=["fenced_code", "tables"])
    
    with open("templates/analiz.html", "w", encoding="utf-8") as f:
        f.write(f"""
        {{% load static %}}
        <!DOCTYPE html>
        <html lang="az">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>FarmAz - Mətn Səhifəsi</title>
            <link rel="icon" href="689ca7b0-31ad-4d1c-8f75-6f7ce3a99aaf.png">
            <link rel="stylesheet" href="{{% static 'analiz.css' %}}">
        </head>
        <body>
            <main class="main-content">
                <div class="container">
                    <section class="text-display-section">
                        <h2 class="section-title">FarmAZ - Analiz Nəticələri</h2>
                        
                        <div class="text-container">
                            <div class="text-content">
                                {html_output}
                            </div>
                        </div>
                    </section>
                </div>
            </main>
        <footer class="footer">
            <div class="container">
                <div class="footer-content">
                    <div class="footer-section">
                        <h4>FarmAZ</h4>
                        <ul>
                            <li><a href="haqqimizda.html">Haqqımızda</a></li>
                            <li><a href="kamanda.html">Komandamız</a></li>
                            <li><a href="xeberler.html">Xəbərlər</a></li>
                        </ul>
                    </div>
                </div>

                <div class="footer-bottom">
                    <p>&copy; 2024 FarmAz. Bütün hüquqlar qorunur. | Azərbaycanın #1 AI Dəstəkli Kənd Təsərrüfatı Platforması</p>
                </div>
            </div>
        </footer>

        <script>
            function toggleNav() {{
                const nav = document.getElementById('nav');
                nav.classList.toggle('active');
            }}

            window.addEventListener('resize', function() {{
                const nav = document.getElementById('nav');
                if (window.innerWidth > 768) {{
                    nav.classList.remove('active');
                }}
            }});
        </script>
        </body>
        </html>
        """)

    