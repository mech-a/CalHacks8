import React from "react";
import { StyleSheet, Text, View, Image, TextInput } from "react-native";
import MapView, { PROVIDER_GOOGLE } from "react-native-maps";

function MapScreen(props) {
  return (
    <View style={styles.container}>
      <View style={styles.topBar}>
        <View style={{ paddingLeft: "5%" }}>
          <Image source={require("../assets/menu.png")} />
        </View>
        <View style={{ justifyContent: "center" }}>
          <View
            style={{
              left: 15,
              position: "absolute",
              backgroundColor: "#C4C4C4",
              height: 40,
              width: 40,
              borderRadius: 20,
            }}
          ></View>
          <View style={{ paddingLeft: 20, position: "absolute" }}>
            <Image source={require("../assets/bear.png")} />
          </View>
        </View>
        <View>
          <Text style={styles.appTitle}>Sather Walks</Text>
        </View>
      </View>
      <MapView
        style={styles.map}
        provider={PROVIDER_GOOGLE}
        showsUserLocation={true}
        initialRegion={{
          latitude: 37.87,
          longitude: -122.27,
          latitudeDelta: 0.05,
          longitudeDelta: 0.05,
        }}
      ></MapView>
      <View style={styles.infoTab}>
        <View style={styles.searchBarDiv}>
          <View
            style={{
              flex: 1,
              alignItems: "center",
              flexDirection: "row",
              bottom: 18,
              justifyContent: "center",
            }}
          >
            <TextInput
              style={styles.searchTextInput}
              placeholder="Search Destination"
            />
            <Image
              style={{ left: 55, position: "absolute" }}
              source={require("../assets/search.png")}
            />
          </View>
        </View>
        <View style={styles.timeTableDiv}>
          <Text>Leave by</Text>
        </View>
        <View style={styles.goBtnDiv}></View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: "100%",
    height: "100%",
    flexDirection: "column",
  },
  topBar: {
    flex: 1,
    backgroundColor: "#2F80ED",
    alignItems: "center",
    flexDirection: "row",
  },
  map: {
    flex: 8,
  },
  appTitle: {
    fontWeight: "700",
    color: "#FFFFFF",
    alignSelf: "center",
    left: 70,
  },
  infoTab: {
    flex: 7,
  },
  searchBarDiv: {
    flex: 1,
  },
  timeTableDiv: {
    flex: 5,
    backgroundColor: "lightblue",
    flexDirection: "column",
    alignItems: "center",
  },
  goBtnDiv: {
    flex: 2,
    backgroundColor: "red",
  },
  searchTextInput: {
    height: 40,
    margin: 12,
    width: "80%",
    borderWidth: 1,
    backgroundColor: "#FFFFFF",
    paddingLeft: 50,
  },
});

export default MapScreen;
