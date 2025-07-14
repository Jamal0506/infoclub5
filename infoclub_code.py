import streamlit as st

# 페이지 설정
st.set_page_config(page_title="암호 방탈출", layout="centered")
st.title("🎉 축제 암호 방탈출")
st.markdown("""
**컨셉:** 축제를 즐기던 중 이상한 방에 갇히게 되었다.  
노트북 화면에 나오는 암호를 풀고 탈출하라!

---
""")

# 💅 전체 스타일 + 폰트 설정
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', sans-serif !important;
}

/* 일반 본문 텍스트 */
div[data-testid="stMarkdownContainer"] p,
div[data-testid="stMarkdownContainer"] li,
div[data-testid="stMarkdownContainer"] span,
div[data-testid="stText"] {
    font-size: 22px !important;
}

/* 입력창 텍스트 */
div[data-testid="stTextInput"] > div > input {
    font-size: 22px !important;
    height: 40px !important;
}

/* 정답/오답 메시지 */
.feedback {
    font-size: 26px !important;
    font-weight: bold !important;
    margin-top: 10px !important;
    margin-bottom: 20px !important;
}

/* 초록색 힌트 강조 */
.green-hint {
    font-size: 28px !important;
    font-weight: bold !important;
    color: green !important;
}
</style>
""", unsafe_allow_html=True)

# 상태 초기화
if 'stage' not in st.session_state:
    st.session_state.stage = 1

def clear_inputs():
    for key in ["input1", "input2", "input3"]:
        if key in st.session_state:
            del st.session_state[key]

def next_stage():
    st.session_state.stage += 1
    clear_inputs()

# 🧩 1단계
if st.session_state.stage == 1:
    st.header("🧩 첫 번째 암호")
    st.markdown("""
<당신은 축제 도중 정신을 잃었다. 눈을 뜨니 어두운 교실과 교실 한가운데에 덩그러니 놓여있는 노트북이 있다. 화면에는 다음과 같은 문구가 써져있다.>

<span class='green-hint'>(글자속 숨겨진 암호를 찾아 탈출해라)</span>

`준비됐다면 START를 입력하라.`
""", unsafe_allow_html=True)

    answer = st.text_input("노트북 화면에 입력:", key="input1")

    if answer:
        if answer.strip().lower() == "start":
            if "input1" in st.session_state:
                del st.session_state["input1"]
            st.markdown('<p class="feedback" style="color:green;">정답입니다! 다음 방으로 이동하세요.</p>', unsafe_allow_html=True)
            if st.button("다음 방으로 이동"):
                next_stage()
        else:
            st.markdown('<p class="feedback" style="color:red;">오답입니다. 다시 시도하세요.</p>', unsafe_allow_html=True)

# 🔐 2단계
elif st.session_state.stage == 2:
    st.header("🔐 첫 번째 암호")
    st.markdown("""
<화면이 자동으로 넘겨졌다.>

치환 암호표:  
`@=e  $=k  #=n  %=z  *=j  ^=r  !=o  &=y  ~=u  +=q`

암호문: `@#*!&`
""", unsafe_allow_html=True)

    answer = st.text_input("해독된 단어를 입력하세요:", key="input2")

    if answer:
        if answer.strip().lower() == "enjoy":
            if "input2" in st.session_state:
                del st.session_state["input2"]
            st.markdown('<p class="feedback" style="color:green;">정답입니다! 다음 방으로 이동하세요.</p>', unsafe_allow_html=True)
            if st.button("다음 방으로 이동"):
                next_stage()
        else:
            st.markdown('<p class="feedback" style="color:red;">오답입니다. 다시 시도하세요.</p>', unsafe_allow_html=True)

# 🧠 3단계
elif st.session_state.stage == 3:
    st.header("🧠 두 번째 암호")
    st.markdown("""
<화면이 또 자동으로 넘겨졌다.>

암
