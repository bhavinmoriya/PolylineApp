import streamlit as st
import folium
import polyline


def plot_trajectory(coordinates):
    # Create a map centered around the first coordinate
    m = folium.Map(location=coordinates[0], zoom_start=13)

    # Add the trajectory to the map
    folium.PolyLine(coordinates).add_to(m)

    return m


def decode_polyline(encoded_polyline):
    # Decode the polyline
    return polyline.decode(encoded_polyline)


def main():
    st.title("Trajectory Plotter")

    # User input for encoded or decoded geometry
    geometry_type = st.radio("Select Geometry Type:", ("Encoded", "Decoded"))

    if geometry_type == "Encoded":
        encoded_polyline = st.text_input("Enter Encoded Polyline:")
        if st.button("Plot"):
            if encoded_polyline:
                try:
                    decoded_coordinates = decode_polyline(encoded_polyline)
                    m = plot_trajectory(decoded_coordinates)
                    st.write("Trajectory Map:")
                    folium_static(m)
                except Exception as e:
                    st.error(f"Error decoding polyline: {e}")
            else:
                st.warning("Please enter an encoded polyline.")
    else:
        st.write(
            "Enter Decoded Coordinates (as a list of [latitude, longitude] pairs):"
        )
        decoded_input = st.text_area("Example: [[lat1, lon1], [lat2, lon2], ...]")
        if st.button("Plot"):
            try:
                decoded_coordinates = eval(decoded_input)
                if isinstance(decoded_coordinates, list):
                    m = plot_trajectory(decoded_coordinates)
                    st.write("Trajectory Map:")
                    folium_static(m)
                else:
                    st.error(
                        "Invalid input format. Please provide a list of coordinates."
                    )
            except Exception as e:
                st.error(f"Error plotting trajectory: {e}")


# Helper function to display folium map in Streamlit
from streamlit_folium import folium_static

if __name__ == "__main__":
    main()
