import React, { Component } from 'react';
import { StyleSheet, View, Text } from 'react-native';


export default class TestScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }

  render() {
    const cusdata = require('../resources/workouts.json');
    return (
      <Text> {cusdata[20].name} </Text>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});
