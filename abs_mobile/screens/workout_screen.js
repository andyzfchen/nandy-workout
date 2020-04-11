import React, { Component } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import CountDown from 'react-native-countdown-component';
import { THEME_BLUE } from '../styles/main_style';

export default class WorkoutScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
		workout: "Get Ready!",
		time: 3,
		counter: 1
    };
  }

  	preview_exercise() {
		const workout_data = require('../resources/workouts.json');
		var random_num = Math.floor(Math.random() * 38);
		var workout_text = "Up Next: " + workout_data[random_num].name
		this.setState({
			workout: workout_text,
			time: 3,
			counter: this.state.counter + 1
        })
	}

    start_exercise() {
		const workout_data = require('../resources/workouts.json');
		var random_num = Math.floor(Math.random() * 38);
		var workout_text = workout_data[random_num].name
		this.setState({
			workout: workout_text,
			time: 5,
			counter: this.state.counter + 1
        })
    }

  render() {
    return (
      <View style={styles.container}>
		<Text style={styles.workout_text}> {this.state.counter} </Text>
        <Text style={styles.workout_text}> {this.state.workout} </Text>
        <CountDown
            until={this.state.time + 1}
            timeToShow={['S']}
            timeLabels={{s: null}}
            digitStyle={{backgroundColor: THEME_BLUE}}
			digitTxtStyle={{color: '#FFF'}}
			onFinish={() => {
				if(this.state.counter%2 == 0) {
					this.preview_exercise()
				} else {
					this.start_exercise()
				}}}
            // onFinish={() => alert('Congradulations on finishing the workout!')}
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
  workout_text: {
    marginBottom:40,
    fontSize: 40
  }
});
