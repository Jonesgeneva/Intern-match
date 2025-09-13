import streamlit as st
import pandas as pd
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="InternMatch - Smart Internship Recommendation",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
    }
    
    .form-container {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .data-display {
        background: #e3f2fd;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #2196f3;
    }
    
    .internship-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border: 1px solid #ddd;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .success-message {
        background: #d4edda;
        color: #155724;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        border: 1px solid #c3e6cb;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_internships_data():
    """Load internships data from CSV file with caching"""
    try:
        if os.path.exists('internships_dataset.csv'):
            return pd.read_csv('internships_dataset.csv')
        else:
            # Create sample data if CSV doesn't exist
            sample_data = {
                'company': ['TechCorp', 'DataSys', 'WebDev Inc', 'AI Solutions', 'CloudTech', 'FinanceHub', 'GameStudio', 'HealthTech'],
                'position': ['Software Engineer Intern', 'Data Analyst Intern', 'Frontend Developer Intern', 'ML Engineer Intern', 'DevOps Intern', 'Financial Analyst Intern', 'Game Developer Intern', 'Product Manager Intern'],
                'location': ['New York', 'San Francisco', 'Austin', 'Seattle', 'Boston', 'Chicago', 'Los Angeles', 'Remote'],
                'skills_required': ['Python, Java, SQL', 'Python, R, Excel', 'JavaScript, React, HTML', 'Python, TensorFlow, ML', 'AWS, Docker, Python', 'Excel, SQL, Python', 'Unity, C#, Game Design', 'Analytics, Communication, Strategy'],
                'education_level': ['Bachelor', 'Bachelor', 'Bachelor', 'Master', 'Bachelor', 'Bachelor', 'Bachelor', 'Master'],
                'duration': ['3 months', '6 months', '4 months', '6 months', '3 months', '4 months', '6 months', '3 months'],
                'stipend': ['$2000/month', '$1800/month', '$2200/month', '$2500/month', '$1900/month', '$2100/month', '$2300/month', '$2400/month'],
                'description': [
                    'Develop web applications using modern frameworks and collaborate with senior developers',
                    'Analyze business data, create insights, and build interactive dashboards',
                    'Build responsive user interfaces and work on user experience improvements',
                    'Work on cutting-edge machine learning projects and model deployment',
                    'Manage cloud infrastructure, automate deployments, and ensure system reliability',
                    'Conduct financial analysis, create reports, and support investment decisions',
                    'Design and develop engaging games using Unity and participate in the full game development lifecycle',
                    'Assist in product strategy, conduct market research, and coordinate with development teams'
                ]
            }
            df = pd.DataFrame(sample_data)
            df.to_csv('internships_dataset.csv', index=False)
            return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎯 InternMatch</h1>
        <h3>Smart Internship Recommendation Engine</h3>
        <p>Find the perfect internship match for your skills and interests</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create tabs for better organization
    tab1, tab2 = st.tabs(["📝 Application Form", "📊 Internships Database"])
    
    with tab1:
        st.markdown('<div class="form-container">', unsafe_allow_html=True)
        st.subheader("Tell us about yourself")
        
        # Create form
        with st.form("internship_form"):
            # Personal Information
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Full Name *", placeholder="Enter your full name")
                education = st.selectbox(
                    "Education Level *",
                    ["", "High School", "Bachelor's (1st Year)", "Bachelor's (2nd Year)", 
                     "Bachelor's (3rd Year)", "Bachelor's (4th Year)", "Master's", "PhD"]
                )
                location = st.text_input("Preferred Location *", placeholder="e.g., New York, San Francisco, Remote")
            
            with col2:
                experience_level = st.selectbox(
                    "Experience Level *",
                    ["", "Beginner (0-1 years)", "Intermediate (1-2 years)", "Advanced (2+ years)"]
                )
                preferred_duration = st.selectbox(
                    "Preferred Duration *",
                    ["", "3 months", "4 months", "6 months", "12 months"]
                )
            
            # Skills and Interests
            skills = st.text_area(
                "Technical Skills *", 
                placeholder="e.g., Python, JavaScript, React, SQL, Machine Learning, Data Analysis...",
                height=100
            )
            
            interests = st.text_area(
                "Areas of Interest *", 
                placeholder="e.g., Web Development, Data Science, Machine Learning, Mobile Apps, Finance...",
                height=100
            )
            
            # Submit button
            submitted = st.form_submit_button("🔍 Submit Application", use_container_width=True)
            
            if submitted:
                # Validation
                if not all([name, education, skills, location, interests, experience_level, preferred_duration]):
                    st.error("❌ Please fill in all required fields!")
                else:
                    # Store form data in session state
                    user_data = {
                        'name': name,
                        'education': education,
                        'skills': skills,
                        'location': location,
                        'interests': interests,
                        'experience_level': experience_level,
                        'preferred_duration': preferred_duration,
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    
                    st.session_state.user_data = user_data
                    st.success("✅ Application submitted successfully!")
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Display submitted data if available
        if 'user_data' in st.session_state:
            st.markdown("---")
            st.subheader("📋 Your Submitted Information")
            
            user_data = st.session_state.user_data
            
            st.markdown('<div class="data-display">', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Name:** {user_data['name']}")
                st.write(f"**Education:** {user_data['education']}")
                st.write(f"**Location:** {user_data['location']}")
                st.write(f"**Experience:** {user_data['experience_level']}")
            
            with col2:
                st.write(f"**Duration:** {user_data['preferred_duration']}")
                st.write(f"**Submitted:** {user_data['timestamp']}")
            
            st.write(f"**Skills:** {user_data['skills']}")
            st.write(f"**Interests:** {user_data['interests']}")
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.subheader("📚 Available Internships")
        
        # Load and display internships data
        internships_df = load_internships_data()
        
        if not internships_df.empty:
            # Add filters
            col1, col2, col3 = st.columns(3)
            
            with col1:
                location_filter = st.selectbox(
                    "Filter by Location",
                    ["All"] + list(internships_df['location'].unique())
                )
            
            with col2:
                duration_filter = st.selectbox(
                    "Filter by Duration", 
                    ["All"] + list(internships_df['duration'].unique())
                )
            
            with col3:
                education_filter = st.selectbox(
                    "Filter by Education",
                    ["All"] + list(internships_df['education_level'].unique())
                )
            
            # Apply filters
            filtered_df = internships_df.copy()
            if location_filter != "All":
                filtered_df = filtered_df[filtered_df['location'] == location_filter]
            if duration_filter != "All":
                filtered_df = filtered_df[filtered_df['duration'] == duration_filter]
            if education_filter != "All":
                filtered_df = filtered_df[filtered_df['education_level'] == education_filter]
            
            st.write(f"Showing {len(filtered_df)} internship(s)")
            
            # Display internships as cards
            for _, internship in filtered_df.iterrows():
                st.markdown('<div class="internship-card">', unsafe_allow_html=True)
                
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"### {internship['position']}")
                    st.markdown(f"**Company:** {internship['company']}")
                    st.markdown(f"**Location:** {internship['location']}")
                    st.markdown(f"**Skills Required:** {internship['skills_required']}")
                    st.markdown(f"**Description:** {internship['description']}")
                
                with col2:
                    st.markdown(f"**Duration:** {internship['duration']}")
                    st.markdown(f"**Stipend:** {internship['stipend']}")
                    st.markdown(f"**Education:** {internship['education_level']}")
                
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.warning("No internship data available.")
        
        # Display raw data option
        if st.checkbox("Show Raw Data"):
            st.dataframe(internships_df, use_container_width=True)

if __name__ == "__main__":
    main()