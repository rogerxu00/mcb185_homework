echo "Roger Xu"
echo "$USER"

gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "a" | grep -v -E "[^muoacft]+" | grep -E ".{4,}" | wc -l
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "b" | grep -v -E "[^tairnl]+" | grep -E ".{4,}" | wc -l
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "c" | grep -v -E "[^maodin]+" | grep -E ".{4,}" | wc -l
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep "z" | grep -v -E "[^anoigr]+" | grep -E ".{4,}" | wc -l

gunzip -c ~/Code/MCB185/data/jaspar2024_core.transfac.gz | grep -v "^#" | cut -f 3 | sort | uniq -c | sort -n | grep "tax_group"

echo "Utah and Akshat "