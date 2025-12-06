import streamlit as st
import folium
import polyline
from streamlit_folium import folium_static
# from streamlit_folium import st_folium  # <-- updated import


# Default encoded polyline
DEFAULT_ENCODED = "wquhH_xnw@qAjC}DbJuBdEkDrFeBrBu@p@wGxEqHnEiD~BqMjJcHlFmBlA}IxE{M~JiOdLcBbBo@x@oApBmB|DiKtV}@hCe@vBU~AaC`SoBxN{BvSk@|GwBlRyAjMMhBElCBhCLnB`@fF^vCvAxHjChHt@dBvMv^lBjE|FvK|HnP|Rdf@vEjMpB`E~BjDvBlCrDxDrJbJjBvBxC~DjD~CxChCfE|CbFvE~F`GnCxC~ErGpEnF~H`JfAxA|BrEb@tAxDjT~C|PjIng@pCzPb@zEhBxLtCxMxThw@hRlp@vMvc@xi@|lBlB~DrFdGrFhBzAPjABhBIvAQdGuAfBy@`BcA~BkBbEiEfCaDtDgFfB{DrEgNxAiDxMiR|DuFlB}BjAgA|BkAdA["

def plot_trajectory(coordinates):
    """Create a folium map with a polyline trajectory."""
    m = folium.Map(location=coordinates[0], zoom_start=13)
    folium.PolyLine(coordinates, color="blue", weight=4).add_to(m)
    return m


def decode_polyline(encoded_polyline):
    """Decode a Google-style encoded polyline string."""
    return polyline.decode(encoded_polyline)


def main():
    st.set_page_config(page_title="Trajectory Plotter")
    st.title("Trajectory Plotter")

    geometry_type = st.radio("Select Geometry Type:", ("Encoded", "Decoded"))

    if geometry_type == "Encoded":
        encoded_polyline = st.text_input(
            "Enter Encoded Polyline:",
            value=DEFAULT_ENCODED,  # Set default here
        )
        if st.button("Plot"):
            try:
                decoded_coordinates = decode_polyline(encoded_polyline)
                m = plot_trajectory(decoded_coordinates)
                st.write("Trajectory Map:")
                folium_static(m)
                # st_folium(m, width=800, height=600)  # <-- updated call
            except Exception as e:
                st.error(f"Error decoding polyline: {e}")

    else:
        # Automatically decode the default polyline for demo
        default_decoded = decode_polyline(DEFAULT_ENCODED)
        st.write(
            "Enter Decoded Coordinates (as a list of [latitude, longitude] pairs):"
        )
        decoded_input = st.text_area(
            "Example: [[lat1, lon1], [lat2, lon2], ...]",
            value=str(default_decoded),
        )
        if st.button("Plot"):
            try:
                decoded_coordinates = eval(decoded_input)
                if isinstance(decoded_coordinates, list):
                    m = plot_trajectory(decoded_coordinates)
                    st.write("Trajectory Map:")
                    folium_static(m)
                    # st_folium(m, width=800, height=600)  # <-- updated call
                else:
                    st.error(
                        "Invalid input format. Please provide a list of coordinates."
                    )
            except Exception as e:
                st.error(f"Error plotting trajectory: {e}")


if __name__ == "__main__":
    main()
