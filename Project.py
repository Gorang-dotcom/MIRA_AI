import streamlit as st
from mira_sdk import MiraClient, Flow

def generate_essay(topic, length):
    # Initialize the client
    api = st.secrets["API_KEY"]
    client = MiraClient(config={"API_KEY": api})
    
    # Prepare input data
    input_data = {
        "topic": topic,
        "length": length
    }
    
    # Set flow version and name
    version = "1.0.0"
    flow_name = f"@gorang/essay-writer/{version}"
    
    try:
        # Execute the flow
        result = client.flow.execute(flow_name, input_data)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Set page config
    st.set_page_config(
        page_title="Essay Writer",
        page_icon="✍️",
        layout="centered"
    )
    
    # Add header
    st.title("✍️ AI Essay Writer")
    st.markdown("Generate essays on any topic using AI")
    
    # Add input fields
    topic = st.text_area("Enter your essay topic", 
                        placeholder="e.g., The Impact of Climate Change on Global Economics")
    
    length_options = ["Short", "Medium", "Long"]
    length = st.selectbox("Select essay length", length_options)  # Fixed method name here
    
    # Add generate button
    if st.button("Generate Essay", type="primary"):
        if topic:
            with st.spinner("Generating your essay..."):
                # Show progress bar
                progress_bar = st.progress(0)
                for i in range(100):
                    progress_bar.progress(i + 1)
                
                # Generate essay
                result = generate_essay(topic, length)
                
                # Display result
                st.subheader("Generated Essay:")
                st.write(result)
                
                # Add download button
                st.download_button(
                    label="Download Essay",
                    data=str(result),
                    file_name="generated_essay.txt",
                    mime="text/plain"
                )
        else:
            st.error("Please enter a topic for your essay")
    
    # Add footer
    st.markdown("---")
    st.markdown("Made with ❤️ using Mira SDK")

if __name__ == "__main__":
    main()
