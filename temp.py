# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""

import streamlit as st
import pandas as pd
st.text("这是一个普通文本元素")
st.title("作业")
st.title("这是一个标题:raised_hands:",anchor="1",help="提示:smiley_cat:")
st.header("token来:raised_hands::smiley_cat:")
st.subheader("wao	:innocent:")
st.caption("随笔",unsafe_allow_html=True)
st.markdown("随便写写",unsafe_allow_html=False,help="223:innocent:")
st.latex("223124")
data={
      "no.1":[1,2,3],
      "no.2":[5,6,7],
      "no.3":[8,9,0],
   }
index=pd.Series(["第一天","第二天","第三天"],name="天数")
df=pd.DataFrame(data,index=index)
st.subheader("营业表")
st.dataframe(df)
st.dataframe(df,width=400,height=200)
st.dataframe(df,use_container_width=True)