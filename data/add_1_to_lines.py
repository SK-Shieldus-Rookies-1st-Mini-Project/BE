import csv

# 파일 경로
top1m_path = r'c:\SK-Shieldus-Rookies-dev\TeamProject\Zikiring\BE\data\top-1m.csv'
kisa_path = r'c:\SK-Shieldus-Rookies-dev\TeamProject\Zikiring\BE\data\한국인터넷진흥원_피싱사이트_20241231_수정본.csv'
output_path = r'c:\SK-Shieldus-Rookies-dev\TeamProject\Zikiring\BE\data\한국인터넷진흥원_피싱사이트_20241231_수정본_with_top1m.csv'

# 1. top-1m.csv에서 url만 추출
urls = []
with open(top1m_path, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) > 1:
            urls.append(row[1])

# 2. 기존 KISA 파일 읽기
with open(kisa_path, 'r', encoding='utf-8') as f:
    kisa_rows = list(csv.reader(f))

# 3. top-1m url을 첫번째 칼럼, 두번째 칼럼은 0으로 추가
for url in urls:
    kisa_rows.append([url, '0'])

# 4. 결과 저장
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(kisa_rows)

print('완료: 새로운 파일이 저장되었습니다.')