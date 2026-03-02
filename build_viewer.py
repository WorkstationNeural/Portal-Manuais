import os
import html

directory = r"c:\Users\016175\Desktop\Programas\Manuais"

files = {
    "manual-gestao.html": "Manual de Gestão Operacional",
    "manual-ti.html": "Manual de Tecnologia da Informação",
    "manual-staff.html": "Manual do Staff"
}

iframe_templates = []
nav_buttons = []

for i, (f, name) in enumerate(files.items()):
    filepath = os.path.join(directory, f)
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} not found.")
        continue
    with open(filepath, 'r', encoding='utf-8') as f_in:
        content = f_in.read()
    
    escaped_content = html.escape(content, quote=True)
    
    display_style = "block" if i == 0 else "none"
    iframe = f'<iframe id="iframe_{i}" srcdoc="{escaped_content}" style="display: {display_style}; width: 100%; height: 100%; border: none;"></iframe>'
    iframe_templates.append(iframe)
    
    active_class = "active" if i == 0 else ""
    btn = f'<button class="tab-btn {active_class}" onclick="showTab({i})">{name}</button>'
    nav_buttons.append(btn)

viewer_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal de Manuais - Neural</title>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            flex-direction: column;
            background-color: #f4f4f9;
            overflow: hidden;
        }}
        .header {{
            background-color: #075971;
            color: white;
            padding: 15px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            z-index: 10;
        }}
        .header h1 {{
            margin: 0;
            font-size: 1.5em;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .nav-tabs {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .tab-btn {{
            background-color: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: white;
            padding: 8px 16px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
            transition: all 0.3s;
        }}
        .tab-btn:hover {{
            background-color: rgba(255, 255, 255, 0.2);
        }}
        .tab-btn.active {{
            background-color: #0ca5c7;
            border-color: #0ca5c7;
            font-weight: bold;
        }}
        .content-area {{
            flex: 1;
            position: relative;
            background-color: #fff;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2L2 7L12 12L22 7L12 2Z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M2 17L12 22L22 17" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M2 12L12 17L22 12" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            Portal de Manuais
        </h1>
        <div class="nav-tabs">
            {''.join(nav_buttons)}
        </div>
    </div>
    <div class="content-area">
        {''.join(iframe_templates)}
    </div>

    <script>
        function showTab(index) {{
            const iframes = document.querySelectorAll('iframe');
            iframes.forEach(iframe => iframe.style.display = 'none');
            
            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            
            document.getElementById('iframe_' + index).style.display = 'block';
            buttons[index].classList.add('active');
        }}
    </script>
</body>
</html>
"""

output_path = os.path.join(directory, "Portal_de_Manuais.html")
with open(output_path, 'w', encoding='utf-8') as f_out:
    f_out.write(viewer_html)
print(f"Arquivo HTML gerado com sucesso em: {output_path}")

