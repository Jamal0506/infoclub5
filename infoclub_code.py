import streamlit as st

# 현재 단계 선택 (유저가 직접 클릭해서 바꿔야 함)
stage = st.radio("현재 단계 선택", ["1단계", "2단계", "3단계"])

if stage == "1단계":
    st.header("🧩 첫 번째 암호")
    st.markdown("""
    <당신은 축제 도중 정신을 잃었다. 눈을 뜨니 어두운 교실과 교실 한가운데에 덩그러니 놓여있는 노트북이 있다. 화면에는 다음과 같은 문구가 써져있다.>

    :green[(글자속 숨겨진 암호를 찾아 탈출해라)]

    `준비됐다면 START를 입력하라.`
    """)
    answer = st.text_input("노트북 화면에 입력:")
    if answer.strip().lower() == "start":
        st.success("정답입니다! 다음 방으로 이동하세요.")
elif stage == "2단계":
    st.header("🔐 첫 번째 암호")
    st.markdown("""
    <화면이 자동으로 넘겨졌다.>

    치환 암호표:  
    `@=e  $=k  #=n  %=z  *=j  ^=r  !=o  &=y  ~=u  +=q`

    암호문: `@#*!&`
    """)
    answer = st.text_input("해독된 단어를 입력하세요:")
    if answer.strip().lower() == "enjoy":
        st.success("정답입니다! 다음 방으로 이동하세요.")
elif stage == "3단계":
    st.header("🧠 두 번째 암호")
    st.markdown("""
    <화면이 또 자동으로 넘겨졌다.>

    암호문: `ihvwlYdo`

    힌트: `+3`

    알파벳 표:  
    `Plain: a b c d e f g h i j k l m n o p q r s t u v w x y z`

    모든 알파벳은 소문자로 입력하세요.
    """)
    answer = st.text_input("해독된 단어를 입력하세요:")
    if answer.strip().lower() == "festival":
        st.success("🎉 축하합니다! 탈출에 성공했습니다!")
