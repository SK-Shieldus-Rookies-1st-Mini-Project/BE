input_path = r"c:\SK-Shieldus-Rookies-dev\TeamProject\Zikiring\BE\data\한국인터넷진흥원_피싱사이트_20241231.csv"
output_path = r"c:\SK-Shieldus-Rookies-dev\TeamProject\Zikiring\BE\data\한국인터넷진흥원_피싱사이트_20241231_수정본.csv"

with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
    for i, line in enumerate(infile):
        line = line.rstrip("\n")
        if i == 0:
            outfile.write(line + "\n")
        else:
            outfile.write(line + ",1\n")
