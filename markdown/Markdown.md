## Markdown 이란?

* 텍스트 기반의 가벼운 마크업 언어
* 단순한 텍스트 문법으로 작성 가능하며, 다양한 환경에서 변환



## Markdown의 문법

1. ### Heading

   * 문서의 제목이나 소제목으로 사용하며 #을 이용한다.(#뒤에 띄어쓰기 사용)
   * #의 갯수에 따라 크기를 설정 가능하며 h1~h6 까지 설정 가능하다.

2. ### List

   * 순서가 있는 리스트(ol): 1. 2. 3. ...
   * 순서가 없는 리스트(ul): -,*...(띄어쓰기 사용)

3. ### Fenced Code block

   * backtick(`)을 3개 사용하여 작성: ```hello```

   * 특정 언어를 명시하면 Syntax Highlighting 적용 되어 가독성이 좋아짐

     ``` java
     public class hello
         public static void main(String[] args) {
         System.out.println("hello world!")
     }
     ```
   
     
   
4. ### Inline Code block

   * backtick(``) 1개로 생성 가능 

     `hello`

5. ### Link

   * [문자열](url 을 통해서 링크를 작성 가능

     [네이버](www.naver.com)

   * ![문자열](url 을 통해서 이미지도 사용 가능
   
     ![bonono](Markdown.assets/bonono.jpg)
   
   * '>'를 통해 인용문 작성
   
     > hello world
   
7. ### Table

   * 본문- 표를 통해서 사용가능(ctrl +t)

8. ### Text 강조

   * **를 통해서 굵게, 

9. ### 수평선

   * 3개이상의 ***(asterisks), dashes(---),___(underscores)