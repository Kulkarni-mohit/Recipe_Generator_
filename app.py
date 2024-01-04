import streamlit as st
import os
from loadingmodel import recognize
from recipeGenerator import generate_recipe_suggestion
import PIL

# streamlit run app.py
def main():
    image = PIL.Image.open("unnamed.png")
    new_image = image.resize((200, 200))
    st.image(new_image)
    st.title("Recipe Generator App")
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        file_name = uploaded_file.name
        os.makedirs("uploaded_images", exist_ok=True)
        file_path = os.path.join("uploaded_images", file_name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        st.image(uploaded_file, caption="Uploaded Image.")

        cuisine = st.text_input(
            "Enter Cuisine you would prefer... 👇",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
        )

        if st.button("Generator"):
            st.markdown("## Recipe")

            with st.status("Cooking Your Request...", expanded=True) as status:
                st.write("Classifing the image...")
            
                item = recognize(file_path)
                st.write(f"You have uploaded the image of {item[0]}! Delicious 😋")
                
                
                st.write("Generating Delicious Recipe...")

                lis = ["Tomato (Chopped)", "Onion (Chopped)", "Ginger-Garlic Paste"]
                st.write(generate_recipe_suggestion(item, cuisine, "message"))
                
                status.update(label="My work Done now yours started... Get ready with Apron", state="complete", expanded=True)
                    
                
           

if __name__ == '__main__':
    main()
