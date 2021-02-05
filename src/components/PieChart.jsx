import { Pie } from 'react-chartjs-2';
import React, { Component } from 'react';
import { render } from 'react-dom';

const options = {
    maintainAspectRatio: false,
    responsive: false,
    legend: {
        position: 'right',
        labels: {
        boxWidth: 10
        }
    }
}

class PieChart extends Component {

    constructor(props) {
        super(props)
        this.state = {
            labels: ['Test1', 'Test2', 'Test3'],
            datasets: [{
                data: [1000, 200, 4000],
                backgroundColor: ['#347deb', '#eb9c34', '#70b823']
            }]
        }
    }


render() {
    return (
        <div style={{position: 'relative'}}>
            <Pie
                data={{
                    labels: this.state.labels,
                    datasets: this.state.datasets
                }}
                options={options}
            />
            <br />
        </div>
    )
    }
}

export {PieChart};
