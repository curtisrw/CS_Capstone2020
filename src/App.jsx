import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { HomeQueryForm, Graphs } from './components';

const now = new Date();
const yesterdayBegin = new Date(now.getFullYear(), now.getMonth(), now.getDate() - 1);
const todayEnd = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 23, 59, 59, 999);

class App extends Component {
    constructor(props) {
        super(props);
        this.handleSubmit  = this.handleSubmit.bind(this);
        this.state = {
            dateRangeSelection: [yesterdayBegin, todayEnd],
            intemp: [],
            outtemp: [],
            settemp: [],
            hvac_cost: [],
            power_con: [],
            power_cost: [],
            water_con: [],
            water_cost: [],
            stylePath: '/static/css/styles.css'
        };
    }


    renderGraphs() {
        const { intemp, outtemp, settemp, hvac_cost, power_con, power_cost, water_con, water_cost} = this.state;
        return ((
            intemp.length > 0 ||
            outtemp.length > 0 ||
            settemp.length > 0 ||
            hvac_cost.length > 0 ||
            power_con.length > 0 ||
            power_cost.length > 0 ||
            water_con.length > 0 ||
            water_cost.length > 0))
            ? <Graphs
                intemp={intemp}
                outtemp={outtemp}
                settemp={settemp}
                hvac_cost={hvac_cost}
                power_con={power_con}
                power_cost={power_cost}
                water_con={water_con}
                water_cost={water_cost}
            /> : null;
    }

    render() {
        return (
            <div className="">
                <h1>Smarthome Information</h1>
                <HomeQueryForm
                    updateParentComponent={(userData) => this.handleIncomingData(userData)}
                />
                { this.renderGraphs() }
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));
