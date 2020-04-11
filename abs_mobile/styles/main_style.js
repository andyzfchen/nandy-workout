import { StyleSheet} from 'react-native';

export const mainStyle = StyleSheet.create({
  flexOne: {
    flex: 1,
  },
  rowCenteredLayout: {
    alignItems: 'center',
  },
  colCenteredLayout: {
    justifyContent: 'center',
  },
  rowFlexLayout: {
    display: 'flex',
    flexDirection: 'row',
  },
  colFlexLayout: {
    display: 'flex',
    flexDirection: 'column',
  },
});

export const THEME_BLUE = '#55abef';
