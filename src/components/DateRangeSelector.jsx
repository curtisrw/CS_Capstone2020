import React, { Component } from 'react';
import Form from 'react-bootstrap/Form';
import Col from 'react-bootstrap/Col';

import DateRangePicker from '@wojtekmaj/react-daterange-picker';

class DateRangeSelector extends Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
        // this.onTemperatureChange = this.onTemperatureChange.bind(this)
        // this.onSubmit = this.onSubmit.bind(this);
    }

    handleChange(e) {
        this.props.onDateRangeChange(e);
    }

    render() {
        // const { value } = this.state;
        const dateRangeSelection = this.props.dateRangeSelection;

        return (
            <div>
                <div className='container-top'>
                    <Col>
                        <h3 style={{ textAlign: "center" }}>Select Date Range</h3>
                    </Col>
                </div>
                <div className='container-bottom' >
                    <Col style={{ textAlign: "center" }}>
                        <p>
                            Please select a range of time you wish to check on
                        </p>
                        {/* <br /> */}
                        <div className='container'>
                            <DateRangePicker
                                rangeDivider=' to '
                                onChange={this.handleChange}
                                value={dateRangeSelection}
                            />
                        </div>
                    </Col>
                </div>
            </div >
        );
    }
}

export { DateRangeSelector };
