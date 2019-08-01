import React from 'react';

// FeatureLogImg source
import flSmall from './images/icons/log_25.png';
import flMedium from './images/icons/log_51.png';
import flLarge from './images/icons/log_102.png';

// FeatureAlertImg
import fASmall from './images/icons/alert_25.png';
import fAMedium from './images/icons/alert_51.png';
import fALarge from './images/icons/alert_102.png';

// FeatureReportImg
import fRepSmall from './images/icons/report_25.png';
import fRepMedium from './images/icons/report_51.png';
import fRepLarge from './images/icons/report_102.png';

// FeatureRestrictImg
import fResSmall from './images/icons/restrict_25.png';
import fResMedium from './images/icons/restrict_51.png';
import fResLarge from './images/icons/restrict_102.png';

// ComputerTabletImg
import computerTabletSmall from './images/computertablet_150x96.png';
import computerTabletMedium from './images/computertablet_300x192.png';
import computerTabletLarge from './images/computertablet_600x384.png';

// BackToTopImg
import backToTopSmall from './images/icons/back_to_top_22.png';
import backToTopMedium from './images/icons/back_to_top_32.png';
import backToTopLarge from './images/icons/back_to_top_65.png';

export class FeatureLogImg extends React.Component {
  state = { currentSrc: '' };

  onLoad = (event) => {
    this.setState({
      currentSrc: event.target.currentSrc
    });
  }
  
  render () {
    return (
      <div>
        <img src={flLarge} srcSet={`${flSmall} 28w, ${flMedium} 56w, ${flLarge} 112w`} 
         sizes="(max-width: 320px) 28px, (max-width: 800px) 56px, 112px" 
         onLoad={this.onLoad} alt="Log icon" />
      </div>
    );
  }
}

export class FeatureAlertImg extends React.Component {
  state = { currentSrc: '' };

  onLoad = (event) => {
    this.setState({
      currentSrc: event.target.currentSrc
    });
  }
  
  render () {
    return (
      <div>
        <img src={fALarge} srcSet={`${fASmall} 28w, ${fAMedium} 56w, ${fALarge} 112w`} 
         sizes="(max-width: 320px) 28px, (max-width: 800px) 56px, 112px" 
         onLoad={this.onLoad} alt="Alert icon" />
      </div>
    );
  }
}

export class FeatureReportImg extends React.Component {
  state = { currentSrc: '' };

  onLoad = (event) => {
    this.setState({
      currentSrc: event.target.currentSrc
    });
  }
  
  render () {
    return (
      <div>
        <img src={fRepLarge} srcSet={`${fRepSmall} 28w, ${fRepMedium} 56w, ${fRepLarge} 112w`} 
         sizes="(max-width: 320px) 28px, (max-width: 800px) 56px, 112px" 
         onLoad={this.onLoad} alt="Report icon" />
      </div>
    );
  }
}

export class FeatureRestrictImg extends React.Component {
  state = { currentSrc: '' };

  onLoad = (event) => {
    this.setState({
      currentSrc: event.target.currentSrc
    });
  }
  
  render () {
    return (
      <div>
        <img src={fResLarge} srcSet={`${fResSmall} 28w, ${fResMedium} 56w, ${fResLarge} 112w`} 
         sizes="(max-width: 320px) 28px, (max-width: 800px) 56px, 112px" 
         onLoad={this.onLoad} alt="Restric icon" />
      </div>
    );
  }
}

export class ComputerTabletImg extends React.Component {
  state = { currentSrc: '' };

  onLoad = (event) => {
    this.setState({
      currentSrc: event.target.currentSrc
    });
  }
  
  render () {
    return (
      <div>
        <img src={computerTabletLarge} srcSet={`${computerTabletSmall} 96w, ${computerTabletMedium} 192w, ${computerTabletLarge} 384w`} 
         sizes="(max-width: 768px) 96px, (max-width: 1200px) 192px, 384px" 
         onLoad={this.onLoad} alt="Log icon" />
      </div>
    );
  }
}

export class BackToTopImg extends React.Component {
  state = { currentSrc: '' };

  onLoad = (event) => {
    this.setState({
      currentSrc: event.target.currentSrc
    });
  }
  
  render () {
    return (
      <div>
        <img src={backToTopLarge} srcSet={`${backToTopSmall} 22w, ${backToTopMedium} 32w, ${backToTopLarge} 65w`} 
         sizes="(max-width: 768px) 22px, (max-width: 1200px) 32px, 65px" 
         onLoad={this.onLoad} alt="Log icon" />
      </div>
    );
  }
}