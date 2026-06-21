import streamlit as st


def render():

    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-badge">AI-Powered Resume Analysis</div>
        <div class="hero-title">ATS Resume Scorer</div>
        <div class="hero-subtitle">Find out why your resume isn't getting past the filter</div>
        <div class="hero-description">
            Upload your resume and a job description. Get a clear score, 
            the exact keywords you're missing, and specific fixes — 
            not generic advice.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Call-to-Action Button
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        if st.button("Analyze My Resume", use_container_width=True, type="primary"):
            st.session_state.current_view = 'scorer'
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Features Overview
    st.markdown('<div class="section-eyebrow">What you get</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Built to find what\'s actually wrong</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-grid">
        <div class="feature-card-new">
            <span class="feature-icon-new">📊</span>
            <div class="feature-title-new">Five-part scoring</div>
            <div class="feature-desc-new">
                Formatting, keywords, content quality, skill validation, 
                and ATS compatibility — scored separately so you know 
                exactly where to focus.
            </div>
        </div>
        <div class="feature-card-new">
            <span class="feature-icon-new">🔍</span>
            <div class="feature-title-new">Skill validation</div>
            <div class="feature-desc-new">
                Listed a skill but never mentioned it in a project? 
                We catch that. Claims without evidence get flagged.
            </div>
        </div>
        <div class="feature-card-new">
            <span class="feature-icon-new">💬</span>
            <div class="feature-title-new">AI-written fixes</div>
            <div class="feature-desc-new">
                Not just "add more keywords" — specific bullet point 
                rewrites and section-by-section suggestions.
            </div>
        </div>
        <div class="feature-card-new">
            <span class="feature-icon-new">📈</span>
            <div class="feature-title-new">Track your progress</div>
            <div class="feature-desc-new">
                Every analysis is saved to your account so you can see 
                how your resume improves across applications.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # How It Works
    st.markdown('<div class="section-eyebrow">Process</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Three steps, under a minute</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="steps-row">
        <div class="step-box">
            <div class="step-num">1</div>
            <div class="step-title">Upload</div>
            <div class="step-desc">PDF, DOC, or DOCX — drag and drop your resume</div>
        </div>
        <div class="step-box">
            <div class="step-num">2</div>
            <div class="step-title">Paste the JD</div>
            <div class="step-desc">Add the job description you're applying to</div>
        </div>
        <div class="step-box">
            <div class="step-num">3</div>
            <div class="step-title">Get your score</div>
            <div class="step-desc">Detailed breakdown plus exactly what to fix</div>
        </div>
    </div>
    """, unsafe_allow_html=True)