import React, { Component } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import { Button } from 'react-native-elements';

//utils
import ScreenWrapper from '../utils/screen_wrapper';
import { mainStyle, THEME_BLUE } from '../styles/main_style';

export default class DashboardScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  }

  render() {
    const {navigate} = this.props.navigation;
    return (
      <ScreenWrapper>
        <View style={styles.container}>
            <Button
              style={styles.button}
              buttonStyle={{backgroundColor: THEME_BLUE}}
              title="Start Workout Now"
              onPress={() => navigate('Workout')}
            />
        </View>
      </ScreenWrapper>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
  