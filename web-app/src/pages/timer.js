import BreakTime from '@/components/breakTime';
import Pomodoro from '@/components/pomodoro';
import styles from '@/styles/Timer.module.css'
import { useEffect, useState } from 'react';
import StretchIntro from '../components/stretchIntro';
import StretchCam from '../components/stretchCam';
import { IoMenu } from "react-icons/io5";
import StretchDone from '../components/stretchDone';
import Link from 'next/link';


const Timer = () => {
    const [isTimerActive, setIsTimerActive] = useState(false);
    const [originalSeconds, setOriginalSeconds] = useState(1500);
    const [secondsLeft, setSecondsLeft] = useState(1500);
    const [timer, setTimer] = useState();
    const [numSessions, setNumSessions] = useState(4);

    const [isBreak, setIsBreak] = useState(false);
    const [breakTimer, setBreakTimer] = useState();
    const [breakSecondsLeft, setBreakSecondsLeft] = useState(300);

    const [isStretch, setIsStretch] = useState(false);
    const [stretchView, setStretchView] = useState("intro")
    const [stretchTimer, setStretchTimer] = useState();
    const [stretchSecondsLeft, setStretchSecondsLeft] = useState(60);
    const [isStretchDone, setIsStretchDone] = useState(false);

    const startTimer = () => {
        setIsTimerActive(true);
        const timerA = setInterval(() => {
            setSecondsLeft((secondsLeft) => secondsLeft - 1);
        }, 1000);
        setTimer(timerA);
    };

    const stopTimer = () => {
        clearInterval(timer);
        setIsTimerActive(false);
        setSecondsLeft(originalSeconds);
        setNumSessions(4);
    }

    const skipTimer = (timerType) => {
        if (timerType === "normal") {
            setSecondsLeft(0);
        } else if (timerType === "break") {
            setBreakSecondsLeft(0);
        }
        else if (timerType === "stretch") {
            setStretchSecondsLeft(0);
        }
    }

    useEffect(() => {
        if (secondsLeft === 0 && numSessions != 0) {
            clearInterval(timer);
            setIsTimerActive(false);
            setSecondsLeft(originalSeconds);
            setNumSessions(numSessions - 1);
            setIsBreak(true);
            startBreakTimer();
        } else if (secondsLeft === 0 && numSessions === 0) {
            clearInterval(timer);
            setIsTimerActive(false);
            setSecondsLeft(originalSeconds);
            setNumSessions(4);
        }
    }, [secondsLeft, timer]);

    useEffect(() => {
        return () => clearInterval(timer);
    }, [timer]);

    const startBreakTimer = () => {
        const timerB = setInterval(() => {
            setBreakSecondsLeft((breakSecondsLeft) => breakSecondsLeft - 1);
        }, 1000);
        setBreakTimer(timerB);
    }

    useEffect(() => {
        if (breakSecondsLeft === 0) {
            clearInterval(breakTimer);
            setIsBreak(false);
            setBreakSecondsLeft(300);
            setIsStretchDone(false);
            if (numSessions > 0) {
                startTimer();
            } else {
                setNumSessions(4);
            }
        }
    }, [breakSecondsLeft, breakTimer])

    const initStretch = () => {
        setIsStretch(true);
        setStretchView("intro");
    }

    const goToStretchView = () => {
        setStretchView("cam");
        startStretchTimer();
    }

    const goToDoneView = () => {
        setStretchView("intro");
        setIsStretchDone(true);
        setIsStretch(false);

    }

    const startStretchTimer = () => {
        const timerC = setInterval(() => {
            setStretchSecondsLeft((stretchSecondsLeft) => stretchSecondsLeft - 1);
        }, 1000);
        setStretchTimer(timerC);
    }

    useEffect(() => {
        if (stretchSecondsLeft === 0) {
            clearInterval(stretchTimer);
            setStretchSecondsLeft(60);
            goToDoneView();

        }
    }, [stretchSecondsLeft, stretchTimer])


    return (
        <>
            <div className={styles.main}>
                <div className={styles.header}>
                    <div className={styles.headerMenu}>
                        <Link href="/"><button className={styles.hamburgerMenuButton}>
                            <IoMenu />
                        </button></Link>
                        <div className={styles.logo}>
                            <img src="../assets/logo.svg" alt="" />
                            <p>Stretch925</p>
                        </div>
                        <div className={styles.pointsBox}>
                            <p>My points: 88</p>
                        </div>
                    </div>

                    <div className={styles.divider}></div>
                </div>
                {
                    (!isBreak) ?
                        <Pomodoro {...{ isTimerActive, setIsTimerActive, secondsLeft, setSecondsLeft, startTimer, stopTimer, numSessions, skipTimer, setNumSessions }} /> :
                        (isStretch) ?
                            <div className={styles.stretchViewContainer}>
                                {(stretchView === "intro") ? <StretchIntro {...{ numSessions, breakSecondsLeft, goToStretchView }} /> : <></>}
                                {(stretchView === "cam") ? <StretchCam {...{ numSessions, breakSecondsLeft, stretchSecondsLeft, goToDoneView, skipTimer }} /> : <></>}
                            </div>
                            :
                            (isStretchDone) ?
                                <StretchDone {...{ numSessions, breakSecondsLeft, skipTimer }} />
                                :
                                <BreakTime {...{ numSessions, breakSecondsLeft, initStretch }} />

                }
            </div>
        </>
    );
}

export default Timer;