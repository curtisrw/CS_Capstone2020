import React, { Component } from 'react';
import { Line } from 'react-chartjs-2';
import { PieChart } from './';

class Graphs extends Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    render() {
        return (
            <div className="graphs-container">
                <h1>Line Chart</h1>
                <div className='horizontal-container'>
                    <Line /> // TODO
                </div>
            </div>
        );
    }
}

export { Graphs };
