import React, { Component } from "react";
import "./app.css";
import pyLogo from "./assets/python.svg";
import reactLogo from "./assets/react.svg";
export default class Index extends Component {
  constructor(props) {
    super(props);
    const _time = {
      hour: "##",
      min: "##",
      sec: "##",
      day: "##",
      month: "##",
      year: "####",
    };
    this.state = {
      time: _time,
      listen: false,
    };
  }
  componentDidMount() {
    this.setState({ listen: true });
    this.updateClock();
  }

  componentWillUnmount() {
    this.setState({ listen: false });
  }

  async updateClock() {
    setInterval(() => {
      const time = this.fetchData();
      time.then((_time) => this.setState({ time: _time }));
    }, 1000);
  }

  async fetchData() {
    let response = await fetch("/getTime");
    let data = await response.json();
    return data;
  }

  dayComponent() {
    return (
      <p>
        {this.state.time.day +
          "/" +
          this.state.time.month +
          "/" +
          this.state.time.year}
      </p>
    );
  }
  hourComponent() {
    return <p>{this.state.time.hour}</p>;
  }
  minComponent() {
    return <p>{this.state.time.min}</p>;
  }
  secComponent() {
    return <p>{this.state.time.sec}</p>;
  }

  render() {
    return (
      <div className="main-body">
        <div className="app-header">React Python Boiler Plate</div>
        <div className="timer-text">
          {this.dayComponent()}
          <div className="clock-text">
            {this.hourComponent()}:{this.minComponent()}:{this.secComponent()}
          </div>
        </div>
        <div className="app-credits">
          <div className="py-logo">
            <img src={pyLogo} alt="" className="footer-image" />
            <img src={reactLogo} alt="" className="footer-image" />
          </div>
          <p>Created By Ian Mugambi</p>
          <a href="https://github.com/Mugambi-Ian/Reactive-Python">Github</a>
        </div>
      </div>
    );
  }
}
