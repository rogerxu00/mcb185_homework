echo "Roger Xu"
echo "$USER"

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "a" | grep -v -E "[^muoacft]" | grep -E ".{4,}" | wc -l

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v -E "[^btairnl]" | grep -E ".{4,}" | wc -l

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "c" | grep -v -E "[^cmaodin]" | grep -E ".{4,}" | wc -l

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "z" | grep -v -E "[^zanoigr]" | grep -E ".{4,}" | wc -l

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -n | grep "tax_group"

echo "Yutong and Akshat"