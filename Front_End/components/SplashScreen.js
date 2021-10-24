import React from "react";
import {
  StyleSheet,
  Text,
  View,
  Image,
  SafeAreaView,
  Button,
} from "react-native";

function SplashScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Image
        style={{ width: "100%", height: "100%", position: "absolute" }}
        source={require("../assets/LandingPage.png")}
      />
      <Button
        style={{ top: 100, position: "absolute" }}
        title="GO"
        color="#FFFFFF"
        onPress={() => navigation.navigate("Map")}
      />
    </View>
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

export default SplashScreen;
