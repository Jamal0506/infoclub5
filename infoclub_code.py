import streamlit as st

# 페이지 설정
st.set_page_config(page_title="암호 방탈출", layout="centered")
st.title("🎉 축제 암호 방탈출")
st.markdown("""
**컨셉:** 축제를 즐기던 중 이상한 방에 갇히게 되었다.  
노트북 화면에 나오는 암호를 풀고 탈출하라!

---
""")

# 단계 상태 저장
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# 입력값 초기화 함수
def clear_inputs():
    for key in ["stage1_input", "stage2_input", "stage3_input"]:
        if key in st.session_state:
            del st.session_state[key]

# ---------------------------
# 1단계 화면
# ---------------------------
if st.session_state.stage == 1:
    st.header("🧩 첫 번째 암호")
    st.markdown("""
<당신은 축제 도중 정신을 잃었다. 눈을 뜨니 어두운 교실과 교실 한가운데에 덩그러니 놓여있는 노트북이 있다. 화면에는 다음과 같은 문구가 써져있다.>

:green[(글자속 숨겨진 암호를 찾아 탈출해라)]

`준비됐다면 START를 입력하라.`
    """)
    answer1 = st.text_input("노트북 화면에 입력:", key="stage1_input")
    if answer1.strip().lower() == "start":
        st.success("정답입니다! 다음 방으로 이동합니다.")
        clear_inputs()
        st.session_state.stage = 2
        st.experimental_rerun()

# ---------------------------
# 2단계 화면
# ---------------------------
elif st.session_state.stage == 2:
    st.header("🔐 두 번째 암호")
    st.markdown("""
<화면이 자동으로 넘겨졌다.>

```
@ = e  
$ = k  
# = n  
% = z  
* = j  
^ = r  
! = o  
& = y  
~ = u  
+ = q
```

> 암호문: `@#*!&`
    """)
    answer2 = st.text_input("해독된 단어를 입력하세요:", key="stage2_input")
    if answer2.strip().lower() == "enjoy":
        st.success("정답입니다! 마지막 방으로 이동합니다.")
        clear_inputs()
        st.session_state.stage = 3
        st.experimental_rerun()

# ---------------------------
# 3단계 화면
# ---------------------------
elif st.session_state.stage == 3:
    st.header("🧠 세 번째 암호")
    st.markdown("""
<화면이 또 자동으로 넘겨졌다.>

> 암호문: `ihvwlYdo`

힌트: `+3`

```
알파벳 표:
Plain:   a b c d e f g h i j k l m n o p q r s t u v w x y z
Shift+3: d e f g h i j k l m n o p q r s t u v w x y z a b c
```

모든 알파벳은 소문자로 입력하세요.
    """)
    answer3 = st.text_input("해독된 단어를 입력하세요:", key="stage3_input")
    if answer3.strip().lower() == "festival":
        st.success("🎉 축하합니다! 탈출에 성공했습니다!")
        st.balloons()
        if st.button("🏁 처음으로 돌아가기"):
            clear_inputs()
            st.session_state.stage = 1
            st.experimental_rerun()
