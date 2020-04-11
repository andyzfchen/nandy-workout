import React, { Component } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import CountDown from 'react-native-countdown-component';
import { THEME_BLUE } from '../styles/main_style';

export default class WorkoutScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }

  render() {
    return (
      <View style={styles.container}>
        <Text style={{marginBottom:40}}> workout text placeholder </Text>
        <CountDown
            until={10}
            timeToShow={['S']}
            timeLabels={{s: null}}
            digitStyle={{backgroundColor: THEME_BLUE}}
            digitTxtStyle={{color: '#FFF'}}
            onFinish={() => alert('finished')}
            size={60}
      />
      </View>
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
