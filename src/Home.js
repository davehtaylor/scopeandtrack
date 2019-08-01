// Home.js
import React from 'react';
import './index.css';
import { FeatureLogImg, FeatureAlertImg, FeatureReportImg, FeatureRestrictImg, 
         ComputerTabletImg, BackToTopImg } from './images.js';
import requestDemo from './requestDemo.js';


// Functions to summon and dismiss the request demo overlay
function requestOverlayOff() {
    document.getElementById("requestDemoOverlay").style.display = "none";
    document.getElementById("backToTopButton").style.display = "block";
}

// Functions to handle the back to top button on the bottom right
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 700 || document.documentElement.scrollTop > 700) {
        document.getElementById("backToTopButton").style.display = "block";
    } else {
        document.getElementById("backToTopButton").style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

class Home extends React.Component {
    render() {
        return (
            <div className="wrapper">
                <div className="topBar">
                    <div className="logo">
                        <a href="/">Scope&Track</a>
                    </div>

                    <div className="nav">
                        <a href="#features">FEATURES</a> &nbsp; | 
                        &nbsp; <a href="#howDoesItWork">HOW DOES IT WORK?</a> &nbsp; | 
                        &nbsp; <a href="#requestDemo">REQUEST DEMO</a> &nbsp; | 
                        &nbsp; <a href="/login">LOGIN</a>
                    </div>
                </div>

                <div className="heroImage">
                    <div className="heroText">
                        <h2>Stop Filling in Reports by Hand</h2>
                        <br/>
                        <h3>Control the Clutter</h3>
                    </div>
                </div>

                <div className="features">
                    <h2 id="features">Features</h2>

                    <ul className="featureWrapper">
                        <li>
                            <div className="featureWrapper_img">
                                <FeatureLogImg />
                            </div>
                        </li>
                        <li>
                            <div className="featureWrapper_text">
                                <h3>Logs All in One Place</h3>
                                <p>
                                    Instead of a cabinet full of binders, Scope&Track 
                                    allows you to keep all of your logs in one place, 
                                    accessable when and where you need it.
                                </p>
                            </div>
                        </li>
                        <li>
                            <div className="featureWrapper_img">
                                <FeatureAlertImg />
                            </div>
                        </li>
                        <li>
                            <div className="featureWrapper_text">
                                <h3>Alerts</h3>
                                <p>
                                    See alerts for when your devices are out of 
                                    compliance and reminders for when regular 
                                    maintenance is scheduled. 
                                </p>
                            </div>
                        </li>
                        <li>
                            <div className="featureWrapper_img">
                                <FeatureReportImg />
                            </div>
                        </li>
                        <li>
                            <div className="featureWrapper_text">
                                <h3>Effortless Reporting</h3>
                                <p>
                                    With a couple of clicks, you can have historical 
                                    reports on your instruments, with customizable 
                                    criteria.
                                </p>
                            </div>
                        </li>
                        <li>
                            <div className="featureWrapper_img">
                                <FeatureRestrictImg />
                            </div>
                        </li>
                        <li>
                            <div className="featureWrapper_text">
                                <h3>Role Restrictions</h3>
                                <p>
                                    Control what your users are able to access 
                                    and modify with our administrative console.
                                    Create different user roles for different
                                    team memebers.
                                </p>
                            </div>
                        </li>
                    </ul>
                </div>

                <div className="howDoesItWork">
                    <h2 id="howDoesItWork">How Does It Work?</h2>

                        <div className="hdiwWrapper">
                            <div className="hdiwImg">
                                <ComputerTabletImg />
                            </div>

                            <div className="hdiwText">
                                <h3>Logs at your Fingertips</h3>
                                <p>
                                    I mean, look at this product. Wouldn’t you want to use it? I do. 
                                    I created the thing, but I’d still like to use it every single day. 
                                    It’s changed my life in ways that I never thought possible.
                                </p>
                                <p>
                                    Best of all, with Dave's Cool Project, you’ll never be lonely. It’s always 
                                    there for you. It always looks out for you. Dealing with bullies at work 
                                    or school? Dave's Cool Project is there. Just tell Dave's Cool Project 
                                    all of your worries, it they’ll be gone. No need to be concerned with the 
                                    minutiae of life. Just relax, enjoy yourself, and let Dave's Cool Project take 
                                    care of the rest. 
                                </p>
                                <p>
                                    You never have to worry again. 
                                </p>
                            </div>
                        </div>

                </div>

                <div className="requestDemo">
                    <h2>Request Demo</h2>

                    <div id="requestDemoText">
                        <p>
                            Like what you see? We can schedule a demo to show you exactly how it works 
                            so you can see the joy for yourself. 
                        </p>
                        <p>
                            Fill in your name and email address below, and one of our account 
                            representatives will be in touch shortly to schedule your presonal 
                            demonstration of Scope&Track.
                        </p>
                    </div>

                    <form id="requestDemoForm">
                        <label htmlFor="nameField">Full Name</label> 
                        <input type="text" id="nameField" placeholder="Jane Doe" />
                        &emsp;
                        <label htmlFor="emailField">Email Address</label>
                        <input type="email" id="emailField" placeholder="jane@doe.com" />
                        <br/>
                        <input type="button" className="indexButton" value="Request Demo" onClick={requestDemo}/>
                    </form>

                </div>

                {/* Overlay to confirm that the demo request has been sent */}
                <div id="requestDemoOverlay" onClick={requestOverlayOff}>
                    <div id="requestDemoOverlayInner">
                        <h3>Thanks!</h3>

                        <p>We'll be in touch soon</p>

                        <button className="indexButton">Close</button>
                    </div>
                </div>

                <div className="footer">
                    <div className="privacyPolicy">
                        Privacy Policy
                    </div>

                    <div className="copyright">
                        &copy; {new Date().getFullYear()} Scope&Track
                    </div>
                </div>

                <button id="backToTopButton" onClick={backToTop}>
                    <BackToTopImg />
                </button>

            </div>
        );
    }
}

export default Home;