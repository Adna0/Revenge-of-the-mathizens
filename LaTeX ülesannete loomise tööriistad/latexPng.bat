latex file.tex
dvips -o file.ps file.dvi
gswin64.exe -sDEVICE=pngmono -sOutputFile="pildid\\pilt%%02d.png" -r600 -dNOPAUSE -dBATCH file.ps