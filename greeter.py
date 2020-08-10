strings = {
    "title": {
        "en": "STUDENT ENROLLMENT FORM",
        "kr": "학생 등록 양식"
    },
    "name": {
        "en": "Please enter your name",
        "kr": "당신의 이름을 입력하세요"
    },    
    "uni": {
        "en": "Please enter your University name",
        "kr": "대학 이름을 입력하십시오"
    },
    "track": {
        "en": "Please enter your study programme",
        "kr": "학습 프로그램을 입력하십시오"
    },
    "dear": {
        "en": "Dear",
        "kr": "소중한"
    },
    "happy": {
        "en": "we are happy to have you in the",
        "kr": "우리는 당신이"
    },
    "track": {
        "en": "track at the",
        "kr": "에서 추적"
    }
}

def main():
  lang = input("[1] - English, 2 - 한국어: ")
  if lang == "2":
    lang = "kr"
  else:
    lang = "en"
    
  print(f"###################################\n{strings['title'][lang]}\n###################################")

  student = input(f"{strings['name'][lang]}: ")
  uni = input(f"{strings['uni'][lang]}: ")
  track = input(f"{strings['track'][lang]}: ")
  
  print(f"{strings['dear'][lang]} {student}, {strings['happy'][lang]} {track} {strings['track'][lang]} {uni}!")
  
main()
