import React from "react";
import {
  StyleSheet,
  Text,
  View,
  Image,
  SafeAreaView,
  Button,
} from "react-native";

function MeetupMessage({ navigation }) {
  return (
    <SafeAreaView style={styles.container}>
      <Image
        style={{ width: "100%", height: "100%", position: "absolute" }}
        source={require("../assets/MatchedMessage.png")}
      />
      <Button
        style={{ top: 200, position: "absolute" }}
        title="GO"
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

export default MeetupMessage;