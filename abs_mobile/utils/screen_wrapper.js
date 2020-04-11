import React from 'react';
import { StyleSheet, View, SafeAreaView } from 'react-native';
import { mainStyle } from '../styles/main_style';

export default class ScreenWrapper extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <SafeAreaView style={mainStyle.flexOne}>
          {this.props.children}
        </SafeAreaView>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginLeft: 20,
    marginRight: 20,
  },
});
