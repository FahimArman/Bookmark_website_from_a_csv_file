# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:29:26 2023

@author: Night
"""

import pandas as pd

df = pd.read_csv('demo.csv')

with open("index.html", "w") as f:
    f.write("<!DOCTYPE html>")
    f.write("\n<html>")
    
    f.write("\n\t<head>")
    f.write("\n\t\t<meta charset = \"utf-8\">")
    f.write("\n\t\t<title>Titttle</title>")
    f.write("\n\t\t<link rel=\"stylesheet\" type=\"text/css\" href=\"css/font.css\" media=\"screen\" />")
    f.write("\n\t\t<link rel=\"shortcut icon\" type=\"image/x-icon\" href=\"image/logo.gif\" />")
    f.write("\n\t</head>")
    
    f.write("\n\n\t<body>")
    
    f.write("\n\t\t<div class=\"wrapper\">")
    for item in range(len(df)):
        f.write("\n\t\t\t<div class=\"content\">")
        f.write("\n\t\t\t\t\t<a href=\"" + df.iloc[item,1] + "\" target=\"_blank\">")
        f.write("\n\t\t\t\t\t\t<p>" + df.iloc[item,0] + "</p>")
        f.write("\n\t\t\t\t\t</a>")
        f.write("\n\t\t\t</div>")
    
    f.write("\n\t\t</div>")
    f.write("\n\t</body>")
    
    f.write("\n</html>")