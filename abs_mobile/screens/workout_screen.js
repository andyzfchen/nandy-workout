import React, { Component } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import CountDown from '../components/countdown';
import { THEME_BLUE } from '../styles/main_style';

export default class WorkoutScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
		workout: "Get Ready!",
		time: 2,
		counter: 0,
		preview: false
    };
  }

  	preview_exercise() {
		const workout_data = require('../resources/workouts.json');
		var random_num = Math.floor(Math.random() * 38);
		var workout_text = workout_data[random_num].name
		this.setState({
			workout: workout_text,
			time: 3,
			counter: this.state.counter + 1,
			preview: true
		})
	}

    start_exercise() {
		this.setState({
			time: 10,
			counter: this.state.counter + 1,
			preview: false
        })
    }

  render() {
	let preview;
	const isPreview = this.state.preview;
	if (isPreview) {
		preview = <Text style={styles.preview_text}> Up Next: </Text>
	}
    return (
      <View style={styles.container}>
		{preview}
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
  preview_text: {
    marginBottom:20,
    fontSize: 30
  },
  workout_text: {
    marginBottom:40,
    fontSize: 40
  }
});
