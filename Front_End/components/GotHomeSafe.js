import React from "react";
import {
  StyleSheet,
  Text,
  View,
  Image,
  SafeAreaView,
  Button,
} from "react-native";

function GotHomeSafe({ navigation }) {
  return (
    <SafeAreaView style={styles.container}>
      <Image
        style={{ width: "100%", height: "100%", position: "absolute" }}
        source={require("../assets/EndMessage.png")}
      />
      <Button
        style={{ position: "absolute", bottom: 500, left: 200}}
        title="YES"
        color="#FFFFFF"
        onPress={() => navigation.navigate("Map")}
      />
      <Button
        style={{ position: "absolute", bottom: 500, right: 200}}
        title="NO"
        color="#FFFFFF"
        onPress={() => navigation.navigate("Map")}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#2F80ED",
    width: "100%",
    height: "100%",
  },
});

export default GotHomeSafe;