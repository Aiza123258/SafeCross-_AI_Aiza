"""
SafeCross AI - Shared UI Design System
Professional, consistent styling across all pages.
"""

import streamlit as st


# ── Color System ─────────────────────────────────────────────────────────────

COLORS = {
    "primary": "#1e3a5f",
    "primary_light": "#2d5a8e",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "info": "#3b82f6",
    "neutral": "#6b7280",
    "bg_light": "#f8fafc",
    "bg_card": "#ffffff",
    "text_primary": "#1f2937",
    "text_secondary": "#6b7280",
    "border": "#e5e7eb",
}

STATUS_COLORS = {
    "SAFE": "#10b981",
    "CAUTION": "#f59e0b",
    "DANGER": "#ef4444",
    "CLEAR": "#6b7280",
    "CRITICAL": "#ef4444",
    "HIGH": "#f59e0b",
    "MEDIUM": "#f59e0b",
    "LOW": "#10b981",
    "NORMAL": "#10b981",
    "ACTIVE": "#3b82f6",
    "SIMULATION": "#f59e0b",
    "READY": "#10b981",
}


# ── Global CSS ───────────────────────────────────────────────────────────────

GLOBAL_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3a5f 0%, #0f2440 100%);
    }
    [data-testid="stSidebar"] .stMarkdown {
        color: #e2e8f0;
    }
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stMarkdown li,
    [data-testid="stSidebar"] .stMarkdown span {
        color: #e2e8f0 !important;
    }
    [data-testid="stSidebar"] h3 {
        color: #ffffff !important;
        font-weight: 600;
        font-size: 0.95rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    [data-testid="stSidebar"] .stAlert {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.15);
        color: #e2e8f0 !important;
    }

    /* Sidebar navigation links */
    [data-testid="stSidebar"] a,
    [data-testid="stSidebar"] a:visited {
        color: #e2e8f0 !important;
    }
    [data-testid="stSidebar"] a:hover {
        color: #ffffff !important;
        background: rgba(255,255,255,0.1) !important;
    }
    [data-testid="stSidebar"] a p,
    [data-testid="stSidebar"] a span,
    [data-testid="stSidebar"] a div {
        color: #e2e8f0 !important;
    }
    [data-testid="stSidebar"] a:hover p,
    [data-testid="stSidebar"] a:hover span,
    [data-testid="stSidebar"] a:hover div {
        color: #ffffff !important;
    }

    /* Selected/active page in sidebar */
    [data-testid="stSidebar"] a[aria-current="page"],
    [data-testid="stSidebar"] a[aria-current="page"]:visited {
        background: rgba(255,255,255,0.15) !important;
        border-left: 3px solid #60a5fa !important;
    }
    [data-testid="stSidebar"] a[aria-current="page"] p,
    [data-testid="stSidebar"] a[aria-current="page"] span,
    [data-testid="stSidebar"] a[aria-current="page"] div {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Sidebar nav header (app name link) */
    [data-testid="stSidebarNav"] a,
    [data-testid="stSidebarNav"] a:visited {
        color: #e2e8f0 !important;
    }
    [data-testid="stSidebarNav"] a:hover {
        color: #ffffff !important;
    }
    [data-testid="stSidebarNav"] p {
        color: #e2e8f0 !important;
    }

    /* Sidebar collapse button */
    [data-testid="stSidebar"] button[kind="header"] {
        color: #e2e8f0 !important;
    }

    .sc-hero {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a8e 50%, #1e3a5f 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(30,58,95,0.25);
        position: relative;
        overflow: hidden;
    }
    .sc-hero::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 60%;
        height: 200%;
        background: radial-gradient(ellipse, rgba(255,255,255,0.05) 0%, transparent 70%);
    }
    .sc-hero h1 {
        margin: 0;
        font-size: 2.8rem;
        font-weight: 700;
        letter-spacing: -0.02em;
    }
    .sc-hero .subtitle {
        font-size: 1.15rem;
        opacity: 0.9;
        margin: 0.5rem 0 0 0;
        font-weight: 400;
    }
    .sc-hero .tagline {
        font-size: 0.9rem;
        opacity: 0.7;
        margin: 1rem 0 0 0;
    }

    .sc-page-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a8e 100%);
        padding: 1.5rem 2rem;
        border-radius: 12px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 16px rgba(30,58,95,0.2);
    }
    .sc-page-header h2 {
        margin: 0;
        font-size: 1.6rem;
        font-weight: 700;
    }
    .sc-page-header p {
        margin: 0.3rem 0 0 0;
        opacity: 0.85;
        font-size: 0.95rem;
    }

    .sc-card {
        background: #ffffff;
        padding: 1.2rem 1.4rem;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
        border: 1px solid #e5e7eb;
        transition: box-shadow 0.2s ease;
    }
    .sc-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .sc-card-accent {
        background: #ffffff;
        padding: 1.2rem 1.4rem;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        border: 1px solid #e5e7eb;
        border-left: 4px solid #3b82f6;
    }

    .sc-metric {
        text-align: center;
        padding: 1rem;
    }
    .sc-metric .label {
        color: #6b7280;
        font-size: 0.8rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.04em;
    }
    .sc-metric .value {
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0.2rem 0;
        line-height: 1.2;
    }
    .sc-metric .sub {
        color: #6b7280;
        font-size: 0.8rem;
    }

    .sc-feature-card {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .sc-feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    }
    .sc-feature-card .icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .sc-feature-card .title {
        font-size: 1rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 0.3rem;
    }
    .sc-feature-card .desc {
        font-size: 0.85rem;
        color: #6b7280;
        line-height: 1.4;
        margin-bottom: 0.8rem;
    }
    .sc-feature-card .status {
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.2rem 0.6rem;
        border-radius: 20px;
        display: inline-block;
    }

    .sc-pipeline-step {
        text-align: center;
        padding: 1rem 0.5rem;
        border-radius: 10px;
        border: 2px solid #e5e7eb;
        background: white;
        transition: all 0.2s ease;
    }
    .sc-pipeline-step.active {
        border-color: #3b82f6;
        background: #eff6ff;
    }
    .sc-pipeline-step .step-icon {
        font-size: 1.5rem;
        margin-bottom: 0.3rem;
    }
    .sc-pipeline-step .step-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: #374151;
    }

    .sc-status-badge {
        display: inline-block;
        padding: 0.2rem 0.7rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }

    .sc-footer {
        text-align: center;
        padding: 2rem 1rem 1rem 1rem;
        margin-top: 3rem;
        border-top: 1px solid #e5e7eb;
        color: #6b7280;
        font-size: 0.85rem;
    }
    .sc-footer .brand {
        font-weight: 600;
        color: #1e3a5f;
        font-size: 0.95rem;
    }

    .sc-section-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #1f2937;
        margin: 1.5rem 0 0.8rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e5e7eb;
    }

    div[data-testid="stMetric"] {
        background: white;
        padding: 0.8rem 1rem;
        border-radius: 8px;
        border: 1px solid #e5e7eb;
    }
</style>
"""


def inject_global_css():
    """Inject the global design system CSS into the page."""
    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


def render_page_header(title: str, subtitle: str = "", icon: str = ""):
    """Render a consistent page header."""
    display_title = f"{icon} {title}" if icon else title
    subtitle_html = f'<p>{subtitle}</p>' if subtitle else ''
    st.markdown(f"""
    <div class="sc-page-header">
        <h2>{display_title}</h2>
        {subtitle_html}
    </div>
    """, unsafe_allow_html=True)


def render_hero(title: str, subtitle: str, tagline: str = ""):
    """Render the hero section for the home page."""
    tagline_html = f'<p class="tagline">{tagline}</p>' if tagline else ''
    st.markdown(f"""
    <div class="sc-hero">
        <h1>{title}</h1>
        <p class="subtitle">{subtitle}</p>
        {tagline_html}
    </div>
    """, unsafe_allow_html=True)


def render_metric_card(label: str, value: str, color: str = "#1e3a5f", sub: str = ""):
    """Render a single metric card."""
    sub_html = f'<div class="sub">{sub}</div>' if sub else ''
    st.markdown(f"""
    <div class="sc-card">
        <div class="sc-metric">
            <div class="label">{label}</div>
            <div class="value" style="color: {color};">{value}</div>
            {sub_html}
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_feature_card(icon: str, title: str, desc: str, status: str, status_color: str = "#10b981"):
    """Render a feature card for the home page grid."""
    st.markdown(f"""
    <div class="sc-feature-card">
        <div class="icon">{icon}</div>
        <div class="title">{title}</div>
        <div class="desc">{desc}</div>
        <span class="status" style="background: {status_color}15; color: {status_color};">{status}</span>
    </div>
    """, unsafe_allow_html=True)


def render_pipeline_step(icon: str, label: str, active: bool = False):
    """Render a single pipeline step."""
    cls = "sc-pipeline-step active" if active else "sc-pipeline-step"
    st.markdown(f"""
    <div class="{cls}">
        <div class="step-icon">{icon}</div>
        <div class="step-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)


def render_footer():
    """Render the professional footer."""
    st.markdown("""
    <div class="sc-footer">
        <div class="brand">SafeCross AI</div>
        <div>Intelligent Road Safety & Emergency Management</div>
        <div style="margin-top: 0.5rem; font-size: 0.8rem;">
            Prototype &bull; AI-assisted &bull; Safety-first
        </div>
        <div style="margin-top: 0.3rem; font-size: 0.75rem; color: #9ca3af;">
            AI-assisted prototype developed for hackathon demonstration.
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_section_title(title: str):
    """Render a consistent section title."""
    st.markdown(f'<div class="sc-section-title">{title}</div>', unsafe_allow_html=True)


def render_status_badge(text: str, color: str = "#6b7280"):
    """Render a status badge."""
    st.markdown(
        f'<span class="sc-status-badge" style="background: {color}15; color: {color};">{text}</span>',
        unsafe_allow_html=True,
    )


def render_sidebar_brand():
    """Render the SafeCross AI brand in the sidebar."""
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0 0.5rem 0; margin-bottom: 0.5rem;">
        <div style="font-size: 1.4rem; font-weight: 700; color: #ffffff; letter-spacing: -0.02em;">
            SafeCross AI
        </div>
        <div style="font-size: 0.75rem; color: rgba(255,255,255,0.6); margin-top: 0.2rem;">
            Road Safety Intelligence
        </div>
    </div>
    """, unsafe_allow_html=True)
