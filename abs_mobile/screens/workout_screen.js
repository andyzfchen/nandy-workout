import React, { Component } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import CountDown from 'react-native-countdown-component';
import { THEME_BLUE } from '../styles/main_style';

export default class WorkoutScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
		workout: "",
		time: 0,
    };
  }
	componentWillMount() {
		this.exercise_init()
	}

	exercise_init() {
		const workout_data = require('../resources/workouts.json');
		var random_num = Math.floor(Math.random() * 38);
		var workout_text = workout_data[random_num].name
		this.setState({
			workout: workout_text,
			time: 4
		})
	}

    workout_selector() {
		this.setState({
			time: 5
		})
		const workout_data = require('../resources/workouts.json');
		var random_num = Math.floor(Math.random() * 38);
		var workout_text = workout_data[random_num].name
		this.setState({
			workout: workout_text,
			time: 0
        })
    }

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.workout_text}> {this.state.workout} </Text>
        <CountDown
            until={this.state.time + 1}
            timeToShow={['S']}
            timeLabels={{s: null}}
            digitStyle={{backgroundColor: THEME_BLUE}}
			digitTxtStyle={{color: '#FFF'}}
			onFinish={() => this.workout_selector()}
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
